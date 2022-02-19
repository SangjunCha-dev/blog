package examples

import (
	"fmt"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/widget"
)

func CheckRadioButton() {
	a := app.New()
	w := a.NewWindow("Hello")

	// label
	label := widget.NewLabel("Hello World!")

	// check button
	checkButton := widget.NewCheck("Check Button",
		func(b bool) {
			msg := fmt.Sprintf("check = %v", b)
			label.SetText(msg)
		})

	// radio button
	options := []string{"1", "2", "3"}
	radioButton := widget.NewRadioGroup(options,
		func(s string) {
			msg := fmt.Sprintf("radio = %s", s)
			label.SetText(msg)
		})

	w.SetContent(
		container.NewVBox(
			label,
			checkButton,
			radioButton,
		),
	)

	w.Resize(fyne.NewSize(300, 200))
	w.ShowAndRun()
}
