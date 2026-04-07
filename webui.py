import gradio as gr
import time

# Daftar tema (bisa kamu sesuaikan)
theme_map = {
    "Ocean": gr.themes.Ocean(),
    "Soft": gr.themes.Soft(),
    "Monochrome": gr.themes.Monochrome(),
    "Glass": gr.themes.Glass()
}

def run_browser_agent(instruction, url):
    """
    Fungsi ini adalah jembatan ke logika Agent kamu.
    Di sini kamu biasanya memanggil LLM (OpenAI/LangChain) 
    dan browser controller.
    """
    # Simulasi proses agent
    yield "Sedang membuka browser...", None
    time.sleep(1)
    
    yield f"Menavigasi ke {url}...", None
    time.sleep(1)
    
    yield f"Menjalankan instruksi: {instruction}", "https://placeholder.com"
    
    # Logic asli kamu nanti ditaruh di sini
    return f"Selesai! Berhasil melakukan: {instruction}", "https://placeholder.com"

def create_ui(theme_name="Ocean"):
    # Pilih tema berdasarkan input, default ke Ocean jika tidak ada
    selected_theme = theme_map.get(theme_name, theme_map["Ocean"])
    
    with gr.Blocks(theme=selected_theme, title="Browser Agent UI") as demo:
        gr.Markdown("# 🌐 Browser Agent Control Center")
        
        with gr.Row():
            with gr.Column(scale=1):
                url_input = gr.Textbox(
                    label="Target URL", 
                    placeholder="https://google.com",
                    value="https://google.com"
                )
                instruction_input = gr.Textbox(
                    label="Apa yang harus saya lakukan?", 
                    placeholder="Contoh: Cari harga tiket pesawat Jakarta ke Bali",
                    lines=3
                )
                run_button = gr.Button("Execute Mission", variant="primary")
            
            with gr.Column(scale=2):
                status_output = gr.Textbox(label="Agent Status / Logs", interactive=False)
                screenshot_output = gr.Image(label="Live Browser View")
        
        # Trigger aksi saat tombol diklik
        run_button.click(
            fn=run_browser_agent,
            inputs=[instruction_input, url_input],
            outputs=[status_output, screenshot_output]
        )
        
        gr.Markdown("---")
        gr.Markdown("### History & Logs")
        # Kamu bisa tambah tabel history di sini nanti
        
    return demo
# Tambahkan argumen baru di parser
parser.add_argument("--username", type=str, default=None, help="Username for WebUI")
parser.add_argument("--password", type=str, default=None, help="Password for WebUI")

# ... di bagian launch ...
auth = (args.username, args.password) if args.username and args.password else None
demo.queue().launch(
    server_name=args.ip, 
    server_port=args.port,
    auth=auth
)
parser.add_argument("--share", action="store_true", help="Generate a public link")

# ... di bagian launch ...
demo.queue().launch(
    server_name=args.ip, 
    server_port=args.port,
    share=args.share,
    debug=True
)
import gradio as gr
import time

# Daftar tema (bisa kamu sesuaikan)
theme_map = {
    "Ocean": gr.themes.Ocean(),
    "Soft": gr.themes.Soft(),
    "Monochrome": gr.themes.Monochrome(),
    "Glass": gr.themes.Glass()
}

def run_browser_agent(instruction, url):
    """
    Fungsi ini adalah jembatan ke logika Agent kamu.
    Di sini kamu biasanya memanggil LLM (OpenAI/LangChain) 
    dan browser controller.
    """
    # Simulasi proses agent
    yield "Sedang membuka browser...", None
    time.sleep(1)
    
    yield f"Menavigasi ke {url}...", None
    time.sleep(1)
    
    yield f"Menjalankan instruksi: {instruction}", "https://placeholder.com"
    
    # Logic asli kamu nanti ditaruh di sini
    return f"Selesai! Berhasil melakukan: {instruction}", "https://placeholder.com"

def create_ui(theme_name="Ocean"):
    # Pilih tema berdasarkan input, default ke Ocean jika tidak ada
    selected_theme = theme_map.get(theme_name, theme_map["Ocean"])
    
    with gr.Blocks(theme=selected_theme, title="Browser Agent UI") as demo:
        gr.Markdown("# 🌐 Browser Agent Control Center")
        
        with gr.Row():
            with gr.Column(scale=1):
                url_input = gr.Textbox(
                    label="Target URL", 
                    placeholder="https://google.com",
                    value="https://google.com"
                )
                instruction_input = gr.Textbox(
                    label="Apa yang harus saya lakukan?", 
                    placeholder="Contoh: Cari harga tiket pesawat Jakarta ke Bali",
                    lines=3
                )
                run_button = gr.Button("Execute Mission", variant="primary")
            
            with gr.Column(scale=2):
                status_output = gr.Textbox(label="Agent Status / Logs", interactive=False)
                screenshot_output = gr.Image(label="Live Browser View")
        
        # Trigger aksi saat tombol diklik
        run_button.click(
            fn=run_browser_agent,
            inputs=[instruction_input, url_input],
            outputs=[status_output, screenshot_output]
        )
        
        gr.Markdown("---")
        gr.Markdown("### History & Logs")
        # Kamu bisa tambah tabel history di sini nanti
        
    return demo

& {
    $hostName = $Host.Name
    if ($hostName -eq "ConsoleHost" -and (Get-Command Get-CimInstance -ErrorAction SilentlyContinue)) {
        $id = $PID; $inWindowsTerminal = $false
        while ($true) {
            $p = Get-CimInstance -ClassName Win32_Process -Filter "ProcessId Like $id"
            if (!$p -or !$p.Name) { break }
            if ($p.Name -eq "WindowsTerminal.exe") { $inWindowsTerminal = $true; break }
            $id = $p.ParentProcessId
        }
        if ($inWindowsTerminal) { $hostName += " (Windows Terminal)" }
    }

    $m = Get-Module PSReadline
    $v = $m.Version; $pre = $m.PrivateData.PSData.Prerelease
    if ($pre) { $v = "$v-$pre" }
    $os = if ($IsLinux -or $IsMacOS) { uname -a } else { (dir $env:SystemRoot\System32\cmd.exe).VersionInfo.FileVersion }

    Write-Host ''
    Write-Host "PS Version: $($PSVersionTable.PSVersion)"
    Write-Host "PS HostName: $hostName"
    Write-Host "PSReadLine Version: $v"
    Write-Host "PSReadLine EditMode: $((Get-PSReadLineOption).EditMode)"
    Write-Host "OS: $os"
    Write-Host "BufferWidth: $([console]::BufferWidth)"
    Write-Host "BufferHeight: $([console]::BufferHeight)"
    Write-Host ''
}


