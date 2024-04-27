# TODO(developer): Vertex AI SDK - uncomment below & run
# pip3 install --upgrade --user google-cloud-aiplatform
# gcloud auth application-default login

import vertexai
from vertexai.generative_models import GenerativeModel, Part

def generate_text(project_id, location):
    # Initialize Vertex AI
    vertexai.init(project=project_id, location=location)
    # Load the model
    multimodal_model = GenerativeModel(model_name="gemini-1.0-pro-vision-001")
    # Query the model
    response = multimodal_model.generate_content(
    [
        # Add an example image
        Part.from_uri(
            "gs://generativeai-downloads/images/scones.jpg", mime_type="image/jpeg"
        ),
        # Add an example query
        "what is shown in this image?",
    ]
    )
    print(response)
    return response.text

generate_text("fs-ds-and-ai-class", "us-central1")