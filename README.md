# 百色靖西家庭打车攻略

2026-10-01至06建议主线，4人，2间房/晚，详尽规划审核稿。

- 阅读：详尽攻略.md
- [网页版文件](web/index.html)：下载仓库后打开此文件，配套图片和PDF已包含。
- 构建预览：dist/index.html
- 完整PDF：output/pdf/baise-family-guide.pdf
- 每日PDF：output/pdf/day-01-2026-10-01.pdf 至 day-06-2026-10-06.pdf
- 权威正文：content/；结构事实：trip.yaml、data/；来源边界：research/

所有班次、酒店和接送均未预订；publish=false，仅本地预览。
构建：.venv/Scripts/python.exe tools/build_day_pdfs.py .，再执行 tools/build_site.py . --output dist。
校验：.venv/Scripts/python.exe tools/validate_trip.py .。

GitHub仓库：https://github.com/alanhsun/baise-2026-10
本次仅上传仓库，尚未启用GitHub Pages。网页仍为规划审核稿，交通与住宿均未预订。
web/是本次生成的完整网页快照；修改content或data后运行构建，再同步dist/到web/。
GitHub Actions会校验源文件并生成可下载的baise-web-guide压缩包；publish=false时不会部署。
