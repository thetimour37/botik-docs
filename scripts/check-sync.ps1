$repo = "C:\Users\user\Documents\Obsidian Vault\Obsidian Vault\Ботик\botik-docs"
Set-Location $repo

git fetch origin main --quiet

$uncommittedRaw = git status --porcelain
$ahead = (git rev-list origin/main..HEAD --count).Trim()
$behind = (git rev-list HEAD..origin/main --count).Trim()

$messages = @()

if ($uncommittedRaw) {
    $count = ($uncommittedRaw -split "`n" | Where-Object { $_.Trim() -ne "" }).Count
    $messages += "Uncommitted changes: $count file(s)"
}
if ([int]$ahead -gt 0) {
    $messages += "$ahead commit(s) not pushed to origin (git push needed)"
}
if ([int]$behind -gt 0) {
    $messages += "origin is $behind commit(s) ahead (git pull needed)"
}

if ($messages.Count -gt 0) {
    Add-Type -AssemblyName System.Windows.Forms
    $text = "botik-docs is out of sync:`n`n" + ($messages -join "`n")
    [System.Windows.Forms.MessageBox]::Show($text, "botik-docs sync check", [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Warning) | Out-Null
}
