# Kiểm tra repo MinhPhuc Toolkit (gọi script Python) và chạy test máy tính.
# Dùng:  pwsh scripts/validate-repo.ps1   (hoặc powershell -File scripts/validate-repo.ps1)
$ErrorActionPreference = "Stop"
$RepoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$python = (Get-Command python -ErrorAction SilentlyContinue)
if ($null -eq $python) { $python = (Get-Command py -ErrorAction SilentlyContinue) }
if ($null -eq $python) { Write-Error "Không tìm thấy Python (cần >= 3.9)"; exit 1 }

& $python.Source (Join-Path $RepoRoot "scripts/kiem_tra_repo.py")
$ok1 = $LASTEXITCODE
& $python.Source -m unittest discover -s (Join-Path $RepoRoot "tools/tinh-toan/tests")
$ok2 = $LASTEXITCODE
if ($ok1 -ne 0 -or $ok2 -ne 0) { exit 1 }
Write-Host "Tất cả kiểm tra đạt."
