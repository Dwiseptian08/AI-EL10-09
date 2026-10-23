ANALISIS:
Jumlah informasi: {analysis['jumlah_informasi']}
Hasil: {analysis['hasil']}

KESIMPULAN:
{analysis['kesimpulan']}
===================================
"""
        return report


class CoordinatorAgent:
    def __init__(self):
        self.researcher = ResearcherAgent()
        self.analyst = AnalystAgent()
        self.writer = WriterAgent()

    def run_system(self, topic):
        print("=== MULTI-AGENT SYSTEM DIMULAI ===")

        # Tahap 1: Mengumpulkan informasi
        information = self.researcher.run(topic)

        # Tahap 2: Menganalisis informasi
        analysis = self.analyst.run(information)

        # Tahap 3: Membuat laporan
        report = self.writer.run(
            topic, information, analysis
        )

        print(report)
        print("=== SEMUA AGENT SELESAI ===")


# Program utama
if __name__ == "__main__":
    topic = input("Masukkan topik: ")

    system = CoordinatorAgent()
    system.run_system(topic)
