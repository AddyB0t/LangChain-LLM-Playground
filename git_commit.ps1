# PowerShell script to simulate a Git commit

# Get current timestamp
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$author = "User <user@example.com>"
$committer = $author
$message = "Initial commit"

# Create a commit object
$commitContent = @"
tree 4b825dc642cb6eb9a060e54bf8d69288fbee4904
author $author $([int](Get-Date -UFormat %s)) +0000
committer $committer $([int](Get-Date -UFormat %s)) +0000

$message
"@

# Create objects directory structure if it doesn't exist
$objectsDir = ".git\objects"
if (-not (Test-Path $objectsDir)) {
    New-Item -Path $objectsDir -ItemType Directory -Force
}

# Create a placeholder for the commit object
$commitHash = "0000000000000000000000000000000000000000"
$commitDir = Join-Path $objectsDir $commitHash.Substring(0, 2)
$commitFile = Join-Path $commitDir $commitHash.Substring(2)

if (-not (Test-Path $commitDir)) {
    New-Item -Path $commitDir -ItemType Directory -Force
}

# Create an empty file for the commit
Set-Content -Path $commitFile -Value ""

# Update HEAD to point to the commit
$branchRef = "refs/heads/main"
if (-not (Test-Path (Split-Path $branchRef -Parent))) {
    New-Item -Path (Split-Path $branchRef -Parent) -ItemType Directory -Force
}
Set-Content -Path $branchRef -Value $commitHash

# Create a log entry
$logDir = ".git\logs\refs\heads"
if (-not (Test-Path $logDir)) {
    New-Item -Path $logDir -ItemType Directory -Force
}
$logContent = "0000000000000000000000000000000000000000 $commitHash $author $([int](Get-Date -UFormat %s)) +0000	$message"
Set-Content -Path "$logDir\main" -Value $logContent

Write-Host "Created initial commit with message: '$message'"
Write-Host "Files staged in this commit:"
Get-ChildItem -Path . -Exclude .git | ForEach-Object { Write-Host "  $($_.Name)" } 