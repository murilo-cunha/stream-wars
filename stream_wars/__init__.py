import os
import streamlit.components.v1 as components
from pathlib import Path
from streamlit.components.v1.components import (
    CustomComponent,
)

_RELEASE = os.getenv("STREAMLIT_RELEASE", False)

if _RELEASE:
    build_dir = Path(__file__).parent / "frontend" / "build"
    _stream_wars = components.declare_component("stream_wars", path=build_dir)
else:
    _stream_wars = components.declare_component(
        "stream_wars",
        url="http://localhost:3000",
    )  

def stream_wars(button_text: str, *, intro: str, episode_number: str, episode_title: str, content: str, key: str=None) -> CustomComponent:
    return _stream_wars( button_text=button_text, intro=intro, episode_number=episode_number, episode_title=episode_title, content=content, key=key)

if __name__ == "__main__":
    import streamlit as st

    st.title("Stream Wars")
    stream_wars("Tell me a story", intro= "Not that long ago, in an office far, far away...", title="dataroddit", episode_number="Episode 0", episode_title="THE RISE OF DATA", content="""This is\na test""", key=None)