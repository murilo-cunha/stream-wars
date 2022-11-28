"""Documentation page with demo and API."""
import inspect

import pandas as pd
import streamlit as st
from docstring_parser import parse

from stream_wars import _project, stream_wars

st.markdown((_project.parent / "README.md").read_text(), unsafe_allow_html=True)

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
