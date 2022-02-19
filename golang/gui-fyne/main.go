package main

import (
	"gui-fyne/examples"
	"os"
)

func main() {
	// 한글 폰트 지정(실행 파일과 동일경로에 폰트파일 위치)
	err := os.Setenv("FYNE_FONT", "NanumGothic.ttf")
	if err != nil {
		return
	}

	examples.Simple()
	// examples.Dialog()
	// examples.InputButton()
	// examples.CheckRadioButton()
	// examples.ProgressBar()

	// examples.Font()

	// examples.Demo()
}
