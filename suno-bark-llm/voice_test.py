from transformers import AutoProcessor, BarkModel
import scipy
import datetime

print(datetime.datetime.now().strftime('%H:%M:%S'))


processor = AutoProcessor.from_pretrained("suno/bark")
model = BarkModel.from_pretrained("suno/bark")

# Male
voice_preset = "v2/en_speaker_3"
# Female
voice_preset = "v2/en_speaker_9"

inputs = processor("We detect a large Bio in your area! check your surroundings!", voice_preset=voice_preset)

audio_array = model.generate(**inputs)
audio_array = audio_array.cpu().numpy().squeeze()
sample_rate = model.generation_config.sample_rate
scipy.io.wavfile.write("E:\\tinitiate-ai\\suno-bark-llm\\output\\test.wav", rate=sample_rate, data=audio_array)
