package main

import (
	"database/sql"
	"fmt"

	_ "github.com/lib/pq"
)

// User schema or User table
type User struct {
	Id   int
	Name string
	Age  int
}

var (
	db *sql.DB
)

// DB Setting
func InitDB() {
	host := "localhost"
	port := 5432
	name := "TEST"
	user := "test_onwer"
	password := "1234"

	psqlconn := fmt.Sprintf("host=%s port=%d dbname=%s user=%s password=%s sslmode=disable",
		host, port, name, user, password)

	var err error
	db, err = sql.Open("postgres", psqlconn)
	if err != nil {
		panic(err)
	}
}

// DB Connect Test
func ConnectTest() {
	err := db.Ping()
	if err != nil {
		panic(err)
	}
}

func Create(name string, age int) {
	sqlStatement := `INSERT INTO user (name, age) VALUES ($1, $2) returning id`

	stmt, err := db.Prepare(sqlStatement)

	// the inserted id will store in this id
	var id int64

	err = stmt.QueryRow(name, age).Scan(&id)
	if err != nil {
		panic(err)
	}
	fmt.Println("create id :", id)
}

func Read(userId int) {
	sqlStatement := `SELECT "id", "name", "age" FROM "user" WHERE $1 = "id"`
	rows, err := db.Query(sqlStatement, userId)
	if err != nil {
		panic(err)
	}
	defer rows.Close()

	var id int
	var name string
	var age int
	for rows.Next() {
		err := rows.Scan(&id, &name, &age)
		if err != nil {
			panic(err)
		}

		fmt.Printf("id: %d, name: %v, age: %d\n", id, name, age)
	}
}

func Update(id int64, user User) {
	sqlStatement := `UPDATE user SET name=$2, age=$3 WHERE id=$1`

	res, err := db.Exec(sqlStatement, id, user.Name, user.Age)
	if err != nil {
		panic(err)
	}

	rowsAffected, err := res.RowsAffected()
	if err != nil {
		panic(err)
	}

	fmt.Printf("Total rows/record affected %v\n", rowsAffected)
}

func Delete(id int64) {
	sqlStatement := `DELETE FROM user WHERE id=$1`

	res, err := db.Exec(sqlStatement, id)
	if err != nil {
		panic(err)
	}

	rowsAffected, err := res.RowsAffected()
	if err != nil {
		fmt.Println("Error while checking the affected rows.", err)
	} else {
		fmt.Println("Total rows/record affected", rowsAffected)
	}
}

func main() {
	InitDB()

	ConnectTest()

	Create("foo", 10)
	Create("bar", 20)
	Read(1)

	Update(1, User{Name: "foo1", Age: 21})
	Read(1)

	Delete(1)

	defer db.Close()
}
