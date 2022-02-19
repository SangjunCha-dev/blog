package examples

import (
	"time"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/widget"
)

func ProgressBar() {
	a := app.New()
	w := a.NewWindow("Hello")

	// label
	label := widget.NewLabel("Progress Bar")

	// progress bar
	progress := widget.NewProgressBar()
	infProgress := widget.NewProgressBarInfinite()

	go func() {
		for i := 0.0; i <= 100; i++ {
			progress.SetValue(i / 100)
			time.Sleep(time.Millisecond * 100)
		}
	}()

	w.SetContent(
		container.NewVBox(
			label,
			progress,
			infProgress,
		),
	)

	w.Resize(fyne.NewSize(300, 200))
	w.ShowAndRun()
}
