package examples

import (
	"os"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/widget"
)

func Font() {
	// 한글 폰트 지정(실행 파일과 동일경로에 폰트파일 위치)
	os.Setenv("FYNE_FONT", "NanumGothic.ttf")

	a := app.New()
	w := a.NewWindow("Hello")

	hello := widget.NewLabel("안녕하세요")
	w.SetContent(
		container.NewVBox(
			hello,
		),
	)

	w.Resize(fyne.NewSize(300, 200))
	w.ShowAndRun()
}
