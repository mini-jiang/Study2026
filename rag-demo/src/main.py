import os


def load_documents(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    docs = [line.strip() for line in text.split("\n") if line.strip()]
    return docs


def search_documents(question, docs):
    results = []

    for doc in docs:
        score = 0
        for word in question:
            if word in doc:
                score += 1

        if score > 0:
            results.append((score, doc))

    results.sort(reverse=True, key=lambda x: x[0])
    return [doc for score, doc in results[:3]]


def generate_answer(question, related_docs):
    if not related_docs:
        return "知识库中没有找到相关内容。"

    context = "\n".join(related_docs)

    answer = f"""
根据知识库内容，找到以下相关信息：

{context}

针对你的问题：
{question}

可以回答：
{related_docs[0]}
"""
    return answer


def main():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    doc_path = os.path.join(base_dir, "data", "docs.txt")

    docs = load_documents(doc_path)

    print("RAG Demo 启动成功")
    print("输入 exit 退出")

    while True:
        question = input("\n请输入问题：")

        if question == "exit":
            break

        related_docs = search_documents(question, docs)
        answer = generate_answer(question, related_docs)

        print(answer)


if __name__ == "__main__":
    main()