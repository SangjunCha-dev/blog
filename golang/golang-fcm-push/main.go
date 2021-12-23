package main

import (
	"context"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"time"

	firebase "firebase.google.com/go/v4"
	"firebase.google.com/go/v4/messaging"
	"google.golang.org/api/option"
)

var (
	client *messaging.Client
	ctx    context.Context = context.Background()
)

// Firebase APP 초기화
func initApp() {
	var err error

	type AccountKey struct {
		ProjectID string `json:"project_id"`
	}
	accountkey := AccountKey{}

	serviceAccountKeyPath := "./serviceAccountKey.json"

	keyFile, err := ioutil.ReadFile(serviceAccountKeyPath)
	if err != nil {
		fmt.Println("[initApp] setConfig error :", err)
	}
	if err := json.Unmarshal(keyFile, &accountkey); err != nil {
		fmt.Println("[initApp] getConfig error :", err)
	}

	opt := option.WithCredentialsFile(serviceAccountKeyPath)
	config := &firebase.Config{ProjectID: accountkey.ProjectID}

	app, err := firebase.NewApp(ctx, config, opt)
	if err != nil {
		fmt.Println("[initApp] initializing app error :", err)
	}

	// Obtain a messaging.Client from the App.
	client, err = app.Messaging(ctx)
	if err != nil {
		fmt.Println("[initApp] getting Messaging client error :", err)
	}
}

// Firebase Cloud Messaging 단일 전송
func sendNotification(title string, body string, fcmToken string) {

	// This registration token comes from the client FCM SDKs.
	registrationToken := fcmToken

	notification := &messaging.Notification{
		Title: title,
		Body:  body,
	}

	// See documentation on defining a message payload.
	message := &messaging.Message{
		Data: map[string]string{
			"Type":    title,
			"Content": body,
		},
		Token:        registrationToken,
		Notification: notification,
	}

	response, err := client.Send(ctx, message)
	if err != nil {
		fmt.Println("[sendNotification] client.Send error :", err, registrationToken)
	}
	_ = response
}

// Firebase Cloud Messaging 다중 전송
func sendNotifications(title string, body string, fcmTokens []string) {
	// fcm tokens
	registrationTokens := fcmTokens

	notification := &messaging.Notification{
		Title: title,
		Body:  body,
	}

	message := &messaging.MulticastMessage{
		Data: map[string]string{
			"Type":    title,
			"Content": body,
		},
		Tokens:       registrationTokens,
		Notification: notification,
	}

	br, err := client.SendMulticast(ctx, message)
	if err != nil {
		panic(err)
	}

	fmt.Println("[sendNotifications] ", br.SuccessCount, " messages were sent successfully, ", br.FailureCount, " messages fail count")

	if br.FailureCount > 0 {
		var failedTokens []string
		for idx, resp := range br.Responses {
			if !resp.Success {
				// The order of responses corresponds to the order of the registration tokens.
				failedTokens = append(failedTokens, registrationTokens[idx])
			}
		}

		fmt.Printf("[sendNotifications] List of tokens that caused failures: %v\n", failedTokens)
	}
}

func main() {
	title := fmt.Sprintf("%s 알림", time.Now().Format("15:04:05"))
	body := fmt.Sprintf("테스트 메세지")
	fcmToken := fmt.Sprintf("[fcmToken]")

	// 특정 기기에 메시지 전송
	sendNotification(title, body, fcmToken)

	fcmTokens := []string{
		"fcmToken",
	}

	// 여러 기기에 메시지 전송
	sendNotifications(title, body, fcmTokens)
}
