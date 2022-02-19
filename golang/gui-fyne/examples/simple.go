package examples

import (
	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/widget"
)

func Simple() {
	a := app.New()
	w := a.NewWindow("Hello") // 윈도우 명칭 지정

	hello := widget.NewLabel("Hello World!")
	w.SetContent(
		container.NewVBox( // 컨텐츠 수직 정렬
			hello,
			widget.NewButton(
				"Hi!",                                  // 버튼 명칭
				func() { hello.SetText("Welcome :)") }, // 버튼 이벤트
			),
		),
	)

	w.Resize(fyne.NewSize(300, 200))
	w.ShowAndRun() // 윈도우 출력
}
