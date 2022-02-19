package examples

import (
	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/theme"
	"fyne.io/fyne/v2/widget"
)

func InputButton() {
	a := app.New()
	w := a.NewWindow("Hello")

	// label
	label := widget.NewLabel("Hello World!")

	// input
	entry := widget.NewEntry()
	entry.SetPlaceHolder("Entry")

	// input에 입력한 값을 label에 표시하는 버튼
	button := widget.NewButton("Submit Text Button",
		func() {
			label.SetText(entry.Text)
		})

	// input에 입력한 값을 label에 표시하는 아이콘 버튼
	iconButton := widget.NewButtonWithIcon("Submit Icon Button", theme.ConfirmIcon(),
		func() {
			label.SetText(entry.Text)
		})

	w.SetContent(
		container.NewVBox(
			label,
			entry,
			button,
			iconButton,
		),
	)

	w.Resize(fyne.NewSize(300, 200))
	w.ShowAndRun()
}
