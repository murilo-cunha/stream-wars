import os
import streamlit.components.v1 as components
from pathlib import Path

_RELEASE = os.getenv("ST_IS_RELEASE", False)

if not _RELEASE:
    _stream_wars = components.declare_component(
        "stream_wars",
        url="http://localhost:3001",
    )
else:
    build_dir = Path(__file__).parent / "frontend" / "build"
    _stream_wars = components.declare_component("stream_wars", path=build_dir)

def stream_wars(name, key=None):
    return _stream_wars(name=name, key=key, default=0)

if __name__ == "__main__":
    import streamlit as st

    st.subheader("Component with constant args")
    # num_clicks = stream_wars("World")
    # st.markdown("You've clicked %s times!" % int(num_clicks))

    st.markdown("---")
    st.subheader("Component with variable args")

    
    name_input = st.text_input("Enter a name", value="Streamlit")
    num_clicks = 2 #my_component(name_input, key="foo")
    st.markdown("You've clicked %s times!" % int(num_clicks))