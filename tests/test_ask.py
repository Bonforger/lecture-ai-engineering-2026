"""会話履歴を保つ質問スクリプトのテスト（Gemini API は呼び出さない）。"""

import sys
from types import SimpleNamespace

from app import ask


def test_follow_up_questions_share_one_chat(monkeypatch, capsys):
    class FakeChat:
        def __init__(self):
            self.questions = []

        def send_message(self, question):
            self.questions.append(question)
            return SimpleNamespace(text=f"回答: {question}", usage_metadata=None)

    chat = FakeChat()
    created_chats = []

    def create_chat(*, model):
        created_chats.append(model)
        return chat

    client = SimpleNamespace(chats=SimpleNamespace(create=create_chat))
    def create_client(api_key):
        assert api_key == "test-key"
        return client

    monkeypatch.setattr(ask.genai, "Client", create_client)
    monkeypatch.setattr(ask, "get_api_key", lambda: "test-key")
    monkeypatch.setattr(sys, "argv", ["app.ask", "最初の質問"])
    answers = iter(["追加の質問", "exit"])

    def read_input(prompt):
        print(prompt, end="")
        return next(answers)

    monkeypatch.setattr("builtins.input", read_input)

    ask.main()

    assert chat.questions == ["最初の質問", "追加の質問"]
    assert created_chats == [ask.MODEL]
    assert "回答: 最初の質問" in capsys.readouterr().out
