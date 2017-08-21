OutFile "druaga1soundboard.exe"
InstallDir "$PROGRAMFILES\Will9183 Software\Druaga1 Soundboard"
Section
SetOutPath $INSTDIR
File /r main
WriteUninstaller $INSTDIR\uninstaller.exe
	CreateShortCut "$Desktop\Druaga1 Soundboard.lnk" "$INSTDIR\main\main.exe"
	CreateShortCut "$Desktop\Uninstall Druaga1 Soundboard.lnk" "$INSTDIR\uninstaller.exe"
SectionEnd
Section "Uninstall"
Delete $INSTDIR\uninstaller.exe
rmdir /r $INSTDIR
Delete "$Desktop\Druaga1 Soundboard.lnk"
Delete "$Desktop\Uninstall Druaga1 Soundboard.lnk"
SectionEnd