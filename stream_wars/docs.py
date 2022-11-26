"""Documentation page with demo and API."""
import inspect

import pandas as pd
import streamlit as st
from docstring_parser import parse

from stream_wars import project, stream_wars

st.markdown((project.parent / "README.md").read_text())
st.header("Demo")
(txt_input,) = (
    st.text_input(
        "Tell a story",
        value=(
            "Once upon a time, there was a boy that really liked Streamlit and Star"
            " Wars, but couldn't use a Star Wars 'crawl' of his own. He decided to"
            " take matters into his own hands and create a new component. Legend says"
            " our hero still looks for contributions, and that bugs still lurk in the"
            " dark..."
        ),
    ),
)
stream_wars(
    "Magic 🪄",
    intro="Not that long ago, in an office not so far, far away...",
    title="Stream Wars",
    episode_number="Episode 0",
    episode_title="A NEW COMPONENT",
    content=txt_input,
    key=None,
)

# Docs

_docstr = parse(stream_wars.__doc__)
_fdoc = inspect.signature(stream_wars).parameters.values()

df_docstr = pd.DataFrame(
    {
        "Argument": [p.arg_name for p in _docstr.params],
        "Description": [p.description for p in _docstr.params],
    }
).set_index("Argument")
df_fdoc = (
    pd.DataFrame(
        {
            "Argument": [p.name for p in _fdoc],
            "Type": [p.annotation.__name__ for p in _fdoc],
            "Default": [
                p.default if p.default is not inspect._empty else "" for p in _fdoc
            ],
        }
    )
    .fillna(value="None")
    .set_index("Argument")
)

st.header("API:")
st.markdown(_docstr.short_description)
if _docstr.long_description is not None:
    st.markdown(_docstr.long_description)

st.table(pd.concat([df_docstr, df_fdoc], axis=1))

st.header("Source:")
st.code(inspect.getsource(stream_wars), language="python")
