# Define URLs and output paths
$zipUrl = "https://github.com/rhasspy/piper/releases/download/2023.11.14-2/piper_windows_amd64.zip"
$outputZipFile = "piper.zip"
$extractedFolder = "piper"

$voiceFolder = "voice"
$onnxUrl = "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/hfc_female/medium/en_US-hfc_female-medium.onnx"
onnxOutputFile = "$voiceFolder/en_US-hfc_female-medium.onnx"
$jsonUrl = "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/hfc_female/medium/en_US-hfc_female-medium.onnx.json"
$jsonOutputFile = "$voiceFolder/en_US-hfc_female-medium.onnx.json"

# Remove the existing folder if it exists
if (Test-Path $extractedFolder) {
    Remove-Item -Path $extractedFolder -Recurse -Force
}

# Clean up any existing temporary ZIP files
if (Test-Path $outputZipFile) {
    Remove-Item -Path $outputZipFile -Force
}

# Create the voice folder
if (-not (Test-Path $voiceFolder)) {
    New-Item -ItemType Directory -Path $voiceFolder
}

# Download the ZIP file
Invoke-WebRequest -Uri $zipUrl -OutFile $outputZipFile

# Extract the ZIP file
Add-Type -AssemblyName System.IO.Compression.FileSystem
[System.IO.Compression.ZipFile]::ExtractToDirectory($outputZipFile, ".\")

# Clean up the temporary ZIP file
Remove-Item -Path $outputZipFile -Force

# Download the ONNX model
Invoke-WebRequest -Uri $onnxUrl -OutFile $onnxOutputFile

# Download the JSON file
Invoke-WebRequest -Uri $jsonUrl -OutFile $jsonOutputFile
