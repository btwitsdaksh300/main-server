class FAQ:
    faqs = []

    @classmethod
    def get_all(cls):
        return cls.faqs

    @classmethod
    def create(cls, question):
        faq = {"id": len(cls.faqs) + 1, "question": question}
        cls.faqs.append(faq)
        return faq
