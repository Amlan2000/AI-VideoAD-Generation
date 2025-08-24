# tools/video_generation_tool.py
from langchain.tools import tool
import json
import os
import time

@tool("video_generation_tool")
def generate_shoe_video(beat_data: str) -> str:
    """
    Generate AI marketing video for shoe using beat information.
    
    Args:
        beat_data: JSON string with BPM and beat positions from audio analysis
    
    Returns:
        Video generation parameters and output path
    """
    try:
        # Parse the beat data directly
        beats = json.loads(beat_data)
        bpm = beats.get('bpm', 120)
        beat_positions = beats.get('beat_positions', [])
        
        shoe_image_path = "assets/images/shoe.jpeg"
        
        # Create output directory
        os.makedirs("assets/videos", exist_ok=True)
        
        # Generate output filename
        shoe_name = os.path.basename(shoe_image_path).replace('.jpeg', '').replace('.png', '')
        timestamp = int(time.time())
        output_video = f"assets/videos/{shoe_name}_marketing_{timestamp}.mp4"
        
        # Determine video style based on BPM
        if bpm > 100:
            style = "fast-paced, dynamic transitions, energetic camera movements"
        elif bpm > 70:
            style = "smooth transitions, steady camera movements, rhythmic cuts"
        else:
            style = "slow dramatic reveals, elegant transitions, cinematic style"
        
        # Create ComfyUI/Seedance generation parameters
        video_params = {
            "input_image": shoe_image_path,
            "duration": 15,
            "resolution": "1080x1920",
            "fps": 30,
            "style_prompt": f"Professional shoe marketing video, {style}, studio lighting, clean background",
            "bpm": bpm,
            "beat_sync_points": beat_positions[:12],
            "transition_style": "cut on beat" if bpm > 80 else "smooth fade",
            "output_path": output_video
        }
        
        # Save parameters file
        params_file = f"{output_video}.json"
        with open(params_file, "w") as f:
            json.dump(video_params, f, indent=2)
        
        print(f"🎬 Video generation prepared for: {shoe_name}")
        print(f"📊 Style: {style}")
        print(f"🎵 BPM: {bpm} - {len(beat_positions)} beat sync points")
        
        result = {
            "success": True,
            "shoe_image": shoe_image_path,
            "video_style": style,
            "output_video": output_video,
            "parameters_file": params_file,
            "beat_sync_points": len(beat_positions),
            "ready_for_comfyui": True
        }
        
        return json.dumps(result)
        
    except Exception as e:
        print(f"❌ Error in video generation: {str(e)}")
        return json.dumps({"error": str(e), "success": False})
