class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "<empty>"
        if len(strs)==1 and strs[0] == "":
            return ""
        return "<tag>".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "<empty>":
            return []
        if len(s) == 0:
            return [""]
        return s.split("<tag>")
