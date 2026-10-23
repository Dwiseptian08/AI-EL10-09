class ResearcherAgent:
    def run(self, topic):
        print("\n[Researcher Agent] Mengumpulkan informasi...")

        information = [
            f"Topik yang dibahas adalah {topic}.",
            f"{topic} memiliki aspek teknis yang perlu dipelajari.",
            f"{topic} dapat dianalisis berdasarkan manfaat dan tantangannya."
        ]

        return information


class AnalystAgent:
    def run(self, information):
        print("[Analyst Agent] Menganalisis informasi...")

        analysis = {
            "jumlah_informasi": len(information),
            "hasil": "Informasi berhasil dikumpulkan dan siap disusun.",
            "kesimpulan": (
                "Topik perlu dipahami dari konsep dasar, "
                "manfaat, dan tantangan penerapannya."
            )
        }

        return analysis


class WriterAgent:
    def run(self, topic, information, analysis):
        print("[Writer Agent] Membuat laporan...")

        report = f"""
========== HASIL LAPORAN ==========

Topik: {topic}

INFORMASI:
"""

        for i, item in enumerate(information, start=1):
            report += f"{i}. {item}\n"

        report += f"""
