Set oWS = CreateObject("WScript.Shell")
strDesktop = oWS.SpecialFolders("Desktop")
strWorkspace = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)
strBatFile = strWorkspace & "\run_app.bat"

Set oLink = oWS.CreateShortcut(strDesktop & "\Capital Analyzer.lnk")
oLink.TargetPath = strBatFile
oLink.WorkingDirectory = strWorkspace
oLink.Description = "Capital.com Market Analyzer"
oLink.WindowStyle = 1
oLink.Save

WScript.Echo "Desktop shortcut created successfully!"
