import gradio as gr
import requests
import os

#  USE ENV VARIABLE (IMPORTANT FOR AWS)
BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")

UPLOAD_API = f"{BACKEND_URL}/upload/"
QUERY_API = f"{BACKEND_URL}/query/"

SUPPORTED_EXTS = (".pdf", ".txt", ".json", ".md", ".csv")


#  UPLOAD FILES + FOLDER
def upload_files(files, folders):
    all_files = []

    if files:
        all_files.extend(files)

    if folders:
        all_files.extend(folders)

    if not all_files:
        return " Please upload files or folders."

    success_count = 0

    for f in all_files:
        path = f.name if hasattr(f, 'name') else f

        if not str(path).lower().endswith(SUPPORTED_EXTS):
            continue

        try:
            with open(path, "rb") as file_obj:
                filename = os.path.basename(path)

                response = requests.post(
                    UPLOAD_API,
                    files={"file": (filename, file_obj)}
                )

                if response.status_code == 200:
                    success_count += 1

        except Exception as e:
            return f" Upload error: {str(e)}"

    if success_count == 0:
        return " No valid files uploaded."

    return f" {success_count} files uploaded successfully!"


#  CHAT
def chat_fn(message):
    if not message.strip():
        return " Enter a question."

    try:
        response = requests.get(
            QUERY_API,
            params={"q": message}
        )

        if response.status_code == 200:
            return response.json()["answer"]

        return f" Error: {response.text}"

    except Exception as e:
        return f" Connection error: {str(e)}"


#  UI
with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown("#  Enterprise AI Knowledge Assistant")
    gr.Markdown("Upload files or folders and chat with your documents.")

    with gr.Row():

        # LEFT SIDE
        with gr.Column(scale=1):

            gr.Markdown("##  Upload")

            file_input = gr.File(file_count="multiple", label="Upload Files")

            folder_input = gr.File(
                file_count="directory",
                label="Upload Folder"
            )

            upload_btn = gr.Button("Upload & Process", variant="primary")
            upload_status = gr.Textbox(label="Status")

            upload_btn.click(
                upload_files,
                inputs=[file_input, folder_input],
                outputs=upload_status
            )

        # RIGHT SIDE
        with gr.Column(scale=2):

            gr.Markdown("##  Chat")

            query_input = gr.Textbox(
                label="Ask Question",
                placeholder="Ask anything..."
            )

            submit_btn = gr.Button("Ask", variant="primary")

            answer_output = gr.Textbox(
                label="AI Answer",
                lines=8
            )

            submit_btn.click(
                chat_fn,
                inputs=query_input,
                outputs=answer_output
            )

            query_input.submit(
                chat_fn,
                inputs=query_input,
                outputs=answer_output
            )


#  RUN
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)