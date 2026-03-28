"""
title: Example Filter
author: open-webui
author_url: https://github.com/open-webui
funding_url: https://github.com/open-webui
version: 0.1
"""

from pydantic import BaseModel, Field
from typing import Optional


class Filter:
    """
    Filter 類別：用於 Open WebUI 的對話過濾器。
    主要功能是在 API 請求進入前（inlet）和回應送出後（outlet）進行攔截處理。
    """

    class Valves(BaseModel):
        """
        Valves（系統閥門）：由管理員設定的全域參數。
        這些設定會影響所有使用者。
        """
        priority: int = Field(
            default=0, description="過濾器的優先順序，數字越小越優先執行。"
        )
        max_turns: int = Field(
            default=8, description="系統允許的最大對話輪數（管理員上限）。"
        )
        pass

    class UserValves(BaseModel):
        """
        UserValves（使用者閥門）：每位使用者可自行調整的個人參數。
        """
        max_turns: int = Field(
            default=4, description="使用者個人允許的最大對話輪數。"
        )
        pass

    def __init__(self):
        """
        初始化 Filter 物件，載入預設的 Valves 設定。
        """
        # 若要啟用自訂檔案處理邏輯，可取消下方註解。
        # 啟用後，WebUI 會將檔案相關操作交由此類別的方法處理，而非預設流程。
        # self.file_handler = True

        # 建立 Valves 實例，載入系統預設設定值。
        self.valves = self.Valves()
        pass

    def inlet(self, body: dict, __user__: Optional[dict] = None) -> dict:
        #我要取得使用者輸入的內容

        print(f"inlet:{__name__}")      
        print(f"inlet:body:{body}")
        print(f"inlet:user:{__user__}")
        print(f"使用者輸入的內容: {body.get('content', 'No content found')}")
        print(f"使用者輸入的內容: {body.get('content', 'No content found')}")
        print(f"使用者輸入的內容: {body.get('content', 'No content found')}")   
        return body

    def outlet(self, body: dict, __user__: Optional[dict] = None) -> dict:
        """
        outlet（出口攔截器）：在 AI 模型回應之後、送回給使用者之前執行。
        
        功能：
        - 可在此分析或修改 AI 的回應內容
        - 目前僅做 log 記錄，直接回傳原始 body
        
        參數：
        - body: AI 回應的內容
        - __user__: 當前使用者資訊
        
        回傳：
        - 處理後的 body（可在此修改回應內容）
        """
        print(f"outlet:{__name__}")
        print(f"outlet:body:{body}")
        print(f"outlet:user:{__user__}")

        return body
