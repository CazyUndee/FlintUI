$base = "C:\Users\roone.DESKTOP-QK3UG2M\Downloads\projects\FlintUI\packages\win"

# Rename directories
Rename-Item -Path "$base\FlintUI.WinUI" -NewName "CronixUI.WinUI" -Force
Rename-Item -Path "$base\FlintUI.Test" -NewName "CronixUI.Test" -Force

# Rename WinUI project files
Rename-Item -Path "$base\CronixUI.WinUI\FlintUI.WinUI.csproj" -NewName "CronixUI.WinUI.csproj" -Force
Rename-Item -Path "$base\CronixUI.WinUI\FlintUI.WinUI.sln" -NewName "CronixUI.WinUI.sln" -Force

# Rename Test project files  
Rename-Item -Path "$base\CronixUI.Test\FlintUI.Test.csproj" -NewName "CronixUI.Test.csproj" -Force
Rename-Item -Path "$base\CronixUI.Test\FlintUI.Test.sln" -NewName "CronixUI.Test.sln" -Force

# Delete temp script
Remove-Item -Path "C:\Users\roone.DESKTOP-QK3UG2M\Downloads\projects\FlintUI\rename_files.ps1" -Force -ErrorAction SilentlyContinue
