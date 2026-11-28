# 第6回 解答

## 演習

<!-- [tool call] の行は、表示された行をそのまま貼り付けてください。終わらなかった STEP は、空欄のままでかまいません。 -->

- STEP 1 のツールの名前：glossary_search_glossary
- STEP 2 の [tool call]:glossary_search_glossary({'query': '3レベル'})
- STEP 3 の [tool call]： fetch_fetch({'url': 'https://modelcontextprotocol.io/'})
- STEP 4 の [tool call]：aws_aws___search_documentation({'search_phrase': 'Amazon S3 versioning overview', 'topics': ['general']})
- 気づき・疑問：

## 宿題

<!-- 基礎・実装・発展のどれか1つに取り組めば完了です。 -->

- 取り組んだレベル：基礎
- やったこと：以下の行を追加したserver.tool()(tools.get_lecture_summary)
- 結果：以下の出力を得た
---第2回では、**「ファインチューニングとLoRA」**をテーマに学びます。

主な内容は以下の通りです：

1. **事前学習とファインチューニングの違い**
   - 事前学習で汎用的な言語能力を身につけたモデルを、目的に合うデータで追加学習させる仕組みや、向く場面・向かない場面を理解します。
2. **SFT（教師あり微調整）**
   - 入力と望ましい出力のペアを使って学習させる方法を学びます。
3. **PEFTとLoRAの考え方**
   - 全パラメータを更新するのではなく、小さな低ランク行列だけを学習させることで、必要なGPUメモリや保存容量を大幅に削減する「LoRA」の仕組みを学びます。
4. **過学習への注意**
   - 検証データを使って性能を確かめる重要性を学びます。
5. **演習**
   - Google Colab上で小さなモデルをLoRAで学習させ、学習の前後で出力形式や内容の正解率がどう変わるかを体験します。

関係する回：第2回

--- trace ---
[tool call]   glossary_get_lecture_summary({'lecture': 2})
[tool return] glossary_get_lecture_summary -> # 第2回 ファインチューニングとLoRA

## この回のねらい

- 事前学習とファインチューニングの違い、ファインチューニングが向く場面と向かない場面を理解する
- LoRAの考え方を理解し、Google Colab上で小さなモデルを…
[usage] 入力 5,942 tokens / 出力 264 tokens / モデル応答 2 回
---
- 気づき・疑問：
