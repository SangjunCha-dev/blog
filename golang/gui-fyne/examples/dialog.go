package examples

import (
	"errors"
	"fmt"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/dialog"
	"fyne.io/fyne/v2/widget"
)

func Dialog() {
	a := app.New()
	w := a.NewWindow("Hello")

	hello := widget.NewLabel("Hello World!")
	w.SetContent(
		container.NewVBox(
			hello,
			widget.NewButton(
				"ShowInformation",
				func() { // 메시지 박스
					hello.SetText("Welcome :)")
					// dialog.ShowInformation("title", "information message", w)
					informationDialog := dialog.NewInformation("title", "information message", w)
					informationDialog.SetDismissText("확인")
					informationDialog.Show()
				},
			),
			widget.NewButton(
				"ShowConfirm",
				func() { // 메시지 확인/취소 박스
					confirmDialog := dialog.NewConfirm("title", "프로그램을 종료하시겠습니까?", (func(res bool) { fmt.Println(res) }), w)
					confirmDialog.SetDismissText("취소")
					confirmDialog.SetConfirmText("확인")
					confirmDialog.Show()
				},
			),
			widget.NewButton(
				"ShowError",
				func() { // 에러 메시지 박스
					err := errors.New("error message")
					dialog.ShowError(err, w)
				},
			),
		),
	)
	w.Resize(fyne.NewSize(300, 200))
	w.ShowAndRun() // 윈도우 출력
}
