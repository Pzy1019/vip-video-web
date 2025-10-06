# vip_video_web.py
# -*- coding: utf-8 -*-
import streamlit as st
import webbrowser
import datetime

# 获取当前时间和访问 IP（仅 Render 内部，不一定是真实公网 IP）
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.session_state.setdefault("visited", False)

if not st.session_state["visited"]:
    print(f"[访问记录] 页面被访问于 {now}")
    st.session_state["visited"] = True

st.set_page_config(page_title="视频解析器", layout="centered")

st.title("🎬视频解析器")
st.markdown("**仅供学习交流，请勿用于商业用途！**")

# 平台列表
platform_urls = {
    "优酷视频": "https://www.youku.com/",
    "爱奇艺": "https://www.iqiyi.com/",
    "腾讯视频": "https://v.qq.com/",
    "哔哩哔哩": "https://www.bilibili.com/",
    "芒果TV": "https://www.mgtv.com/",
    "乐视视频": "https://www.le.com/",
    "搜狐视频": "https://tv.sohu.com/",
    "1905电影": "https://www.1905.com/",
    "PPTV": "https://www.pptv.com/",
    "AcFun": "https://www.acfun.cn/"
}

# 解析接口
parse_apis = {
    "路线①": "https://www.yemu.xyz/?url=",
    "路线②": "https://www.8090g.cn/?url=",
    "路线③(加载有广告)": "https://im1907.top/?jx=",
    "路线④": "https://jx.playerjy.com/?url=",
    "路线⑤": "https://jx.xmflv.com/?url=",
    "路线⑥": "https://jx.m3u8.tv/jiexi/?url=",
    "路线⑦": "http://www.jzmhtt.com/zdy/vip/?url="
}

# 平台选择
platform = st.selectbox("选择视频平台：", list(platform_urls.keys()))
if st.button("访问该网站"):
    st.markdown(f"[点击打开 {platform}]({platform_urls[platform]})", unsafe_allow_html=True)

# 输入视频链接
url = st.text_input("请输入视频链接：", placeholder="例如：https://v.qq.com/x/cover/...")

# 选择解析路线
api_name = st.selectbox("选择解析路线：", list(parse_apis.keys()))

# 开始解析
if st.button("开始解析"):
    if url.strip():
        parse_url = f"{parse_apis[api_name]}{url}"
        st.success("✅ 点击下方按钮观看解析结果：")
        st.markdown(f"[打开解析视频]({parse_url})", unsafe_allow_html=True)
    else:
        st.warning("请先输入视频链接！")

# 分割线
st.markdown("---")

# 使用说明
with st.expander("📘 使用说明"):
    st.write("""
    1. 点击“访问网站”进入视频网站  
    2. 复制视频播放页的网址  
    3. 粘贴到输入框  
    4. 选择解析接口并点击“开始解析”  
    """)

# 免责声明
with st.expander("⚠️ 免责声明"):
    st.write("""
    - 本软件仅供学习交流使用，严禁用于商业用途  
    - 请支持正版，购买视频网站会员  
    - 本软件不存储任何视频内容  
    - 使用本软件所产生的一切后果由用户自行承担  
    """)




