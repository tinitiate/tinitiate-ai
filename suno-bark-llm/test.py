"""
from transformers import pipeline
import scipy

synthesiser = pipeline("text-to-speech", "suno/bark")
speech = synthesiser("Hello, my dog is cooler than you!", forward_params={"do_sample": True})
scipy.io.wavfile.write("bark_out.wav", rate=speech["sampling_rate"], data=speech["audio"])
"""

from transformers import AutoProcessor, AutoModel
PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
processor = AutoProcessor.from_pretrained("suno/bark")
model = AutoModel.from_pretrained("suno/bark")
inputs = processor(
    text=["Hello, my name is Suno. And, uh — and I like pizza. [laughs] But I also have other interests such as playing tic tac toe."],
    return_tensors="pt",
)
speech_values = model.generate(**inputs, do_sample=True)

pip uninstall -y tensorboard
pip uninstall -y tensorboard-data-server
pip uninstall -y tensorflow-addons
pip uninstall -y tensorflow-estimator
pip uninstall -y tensorflow-gpu
pip uninstall -y tensorflow-io-gcs-filesystem
pip uninstall -y TensorFlowTTS
