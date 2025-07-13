class Config:
    API_ID = 26091026
    API_HASH = "f608d185d836e0405775833c6888922f"
    Token = "7546990711:AAHC8dfxPfzJqJ3LGbF8Yqg_vxTPWYemvac"
    Session = ":memory:"  # You can replace with session string if needed

    App_Name = "superbot-host"  # 👉 your koyeb app name (edit if needed)
    Port = 8080  # ✅ default Koyeb port

    Archive_Channel_ID = -1002897456594  # ✅ your private channel
    Start_Message = "📁 Send me any file and get a direct download link!"
    Bot_Channel = "filmzimovielink"  # Without @

    Link_Root = f"https://{App_Name}.koyeb.app/"
    Download_Folder = "Files"
    Dev_Channel = "shadow_bots"
    Bot_UserName = None  # Will be set by bot after startup

    Part_size = 1024 * 1024  # (1MB)
    Buffer_Size = 512 * 1024  # (512KB)
    Pre_Dl = 1
    Separate_Time = 4
    Sleep_Threshold = 60
    Max_Fast_Processes = 1


class Strings:
    start = Config.Start_Message
    dl_link = "🔗 Download LINK"
    st_link = "🎞 Stream LINK"
    generating_link = "**⏳ Generating Link...**"
    bot_channel = "📢 Bot Channel"
    dev_channel = "🤖 Developer"
    fast = "⚡️**The link has been updated to a fast link**"
    update_link = "⚡ Update To Fast Link"
    update_limited = (f"⛔ You can update just {Config.Max_Fast_Processes} link in one time, "
                      "please wait until previous update to complete")
    re_update_link = "🔄 Re-Updating the link"
    already_updated = "The link is already updated"
    wait_update = "⏳ Updating the link..."
    wait = "⏳ Please wait..."
    progress = "⏳ Progress"
    file_not_found = "⚠️ File Not Found, Please resend it again"
    delete_manually_button = "⚠️ You can delete it"
    delete_forbidden = "❌ Can't delete messages older than 48h, please delete manually"
    force_join = "⚠ Join Bot Channel to use this Bot"
