# PowerShell script to initialize Git repository and add files

# Create config file
$configContent = @"
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[user]
	name = User
	email = user@example.com
"@

Set-Content -Path ".git\config" -Value $configContent

# Create description file
Set-Content -Path ".git\description" -Value "Unnamed repository; edit this file 'description' to name the repository."

# Create index file (empty)
[System.IO.File]::WriteAllBytes(".git\index", [byte[]]@())

# Create info directory and exclude file
New-Item -Path ".git\info" -ItemType Directory -Force
Set-Content -Path ".git\info\exclude" -Value "# git ls-files --others --exclude-from=.git/info/exclude
# Lines that start with '#' are comments.
# For a project mostly in C, the following would be a good set of
# exclude patterns (uncomment them if you want to use them):
# *.[oa]
# *~"

Write-Host "Git repository initialized successfully!" 