import re
import pandas as pd

def remove_html(html):
    # Troca nbsp por espaço vazio
    text = html.replace(' &nbsp; ', ' ')
    text = text.replace('&nbsp; ', ' ')
    text = text.replace(' &nbsp;', ' ')
    text = text.replace('&nbsp;', ' ')
    return re.sub("<[^>]*>", "", text).strip()

def remove_html_and_numbers(html):
    text = re.sub(r'\d+', '', html)
    return remove_html(text)
    
# Além de remover as tags html, tira os &nbsp (troca por espaço) e substitui os parágrafos por \n
def html_to_plain_text(html: str) -> str:
    TAG_RE = re.compile(r"<[^>]+>")
    P_TAG_RE = re.compile(r"<p[^>]*>", flags=re.IGNORECASE)

    if pd.isna(html):
        return ""
    # Substitui <p> e <p ...> por nova linha
    text = P_TAG_RE.sub("\n", html)
    # Remove todas as outras tags
    text = TAG_RE.sub("", text)
    # Troca nbsp por espaço vazio
    text = text.replace(' &nbsp; ', ' ')
    text = text.replace('&nbsp; ', ' ')
    text = text.replace(' &nbsp;', ' ')
    text = text.replace('&nbsp;', ' ')
    return text.strip()