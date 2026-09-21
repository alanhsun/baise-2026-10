# 百色·靖西·南宁家庭旅行执行攻略

2026-10-01至06，3人，1间房/晚。网页和每日PDF以现场速查为主，研究证据保存在research/与data/。

9月21日复核：三人六天山水路线；游客社区的接驳、检票、步行、点餐和入住经验；当前正文3张有明确CC许可的渠洋湖、鹅泉实拍照片（旧路线另5张仅素材留档），逐张标注作者与拍摄时间。S4742、D3782与K9304均已购；D3782与K9304三人实付分别为843元和109元，S4742实付待补；百色梦之源两晚实付757元，靖西尚客优两晚实付570元。返程计划G2955南宁站至虎门，南宁住宿改选南宁站周边。详见[图片署名](media/PHOTO-CREDITS.md)和[社区增补记录](research/community-additions-2026-09-16.md)。

- 阅读：详尽攻略.md（合并版执行手册）
- [网页版文件](web/index.html)：下载仓库后打开此文件，配套图片和PDF已包含。
- 构建预览：dist/index.html
- 完整PDF：output/pdf/baise-family-guide.pdf
- 每日PDF：output/pdf/day-01-2026-10-01.pdf 至 day-06-2026-10-06.pdf
- 权威正文：content/；结构事实：trip.yaml、data/；来源边界：research/

S4742、D3782、K9304、百色梦之源两晚及靖西尚客优两晚均已预订；G2955、南宁住宿和接送尚未预订。公开的是planning_guide规划攻略，不记录私人订单号、乘车人证件或入住人信息。
构建：先运行tools/sync_guide.py更新合并Markdown，再用.venv/Scripts/python.exe tools/build_day_pdfs.py .，最后执行tools/build_site.py . --output dist。
校验：.venv/Scripts/python.exe tools/validate_trip.py .。

GitHub仓库：https://github.com/alanhsun/baise-2026-10
公网地址：https://alanhsun.github.io/baise-2026-10/ 。用户授权启用Pages；三段铁路／城际和百色、靖西四晚住宿已预订，G2955与南宁住宿待订。
web/是本次生成的完整网页快照；修改content或data后运行构建，再同步dist/到web/。
GitHub Actions会校验源文件并生成可下载的baise-web-guide压缩包；publish=true且stage为approved/published时部署。
