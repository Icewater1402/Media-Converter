import ffmpeg
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
supported_formats = {
    1: "mp4",
    2: "avi",
    3: "mkv",
    4: "mov",
    5: "flv",
    6: "wmv"
}
def getFormats():
    print("Formats: ")
    for key, value in supported_formats.items():
        print(f"{key}: {value}")

def getFilePath():
    Tk().withdraw()

    print("Please select the input video file: ")
    input_file = askopenfilename(
        title = "Select Input File",
        filetypes=[("Video Files", "*.mp4 *.avi *.mkv *.mov *.flv *.wmv"), ("All Files", "*.*")]
    )
    if not input_file:
        print("No input file selected.")
        return None, None
    
    # Select output file location
    print("Please select where to save the converted file: ")
    output_file = asksaveasfilename(
        title = "Save as",
        defaultextension=".mp4",
        filetypes=[("MP4 Files", "*.mp4"), ("AVI Files", "*.avi"), ("MKV Files", "*.mkv"),
                    ("MOV Files", "*.mov"), ("FLV Files", "*.flv"), ("WMV Files", "*.wmv")]
    )
    if not output_file:
        print("No output file location selected.")
        return None, None
    
    return os.path.abspath(input_file), os.path.abspath(output_file) 

def convert_file(input_file, output_file):
    try:
        if not input_file or not output_file:
            return "Conversion aborted: Missing input or output file."
        
        #DEBUG
        print(f"Input file path: {input_file}")
        print(f"Output file path: {output_file}")

        ffmpeg.input(input_file).output(output_file).run()
        return f"Conversion successful! File saved at: {output_file}"

    except ffmpeg.Error as e:
        return f"Error during conversion: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"

if __name__ == "__main__":
    getFormats()

    input_file, output_file = getFilePath() 

    if input_file and output_file: 

        result = convert_file(input_file, output_file)
        print(result)