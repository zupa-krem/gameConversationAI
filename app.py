from fastapi import FastAPI, Query
from transformers import pipeline

app = FastAPI()

pipe = pipeline(task="text2text-generation",
                model="google/flan-t5-small",
                num_return_sequences=1,
                max_length=50,
)


@app.get("/generate")
def generate(text: str = Query(..., description="Text to generate from")):
    """
    Using the text2text-generation pipeline from `transformers`, generate text
    from the given input text. The model used is `google/flan-t5-small`, which
    can be found [here](<https://huggingface.co/google/flan-t5-small>).
    """

    print(f"Input text: {text}")

    output = pipe(text)

    print(f"Output: {output}")

    return {"output": output[0]["generated_text"]}