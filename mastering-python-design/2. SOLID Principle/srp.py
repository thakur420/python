#class not following srp
class Report:
    def __init__(self,content:str) -> None:
        self.content = content
    
    # Responsibility 1
    def generate(self):
        print(f"Report Content : {self.content}")

    # Responsibility 2
    def save_to_file(self,filename:str):
        with open(filename,"w") as f:
            f.write(self.content)

#class that follow srp

class Report:
    def __init__(self,content:str) -> None:
        print("working ...")
        self.content = content

    def generate(self):
        print(f"Report Content : {self.content}")

class ReportSaver:
    def __init__(self,report:Report) -> None:
        self.report = report
    
    def save_to_file(self,filename:str):
        with open(filename,"w") as f:
            f.write(self.report.content)

if __name__ == "__main__":
    report = Report("This is the content.")
    report.generate()
    report_saver = ReportSaver(report)
    report_saver.save_to_file("srp_demo.txt")