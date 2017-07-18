SLASH_GOLDGOBLIN1, SLASH_GOLDGOBLIN2 = '/gg', '/goldgoblin';

function SlashCmdList.GOLDGOBLIN(msg, editbox)
	if GoldGoblinData[GetRealmName()] ~= nil then
		DEFAULT_CHAT_FRAME:AddMessage("Prospecting data for |cFFFFFF00" .. GetRealmName());
		for k, v in ipairs(GoldGoblinData[GetRealmName()]) do
			for key, value in pairs(v) do
				DEFAULT_CHAT_FRAME:AddMessage("|cFF00FF00" .. key .. ": |r" .. value);
			end
		end
	else
		DEFAULT_CHAT_FRAME:AddMessage("There is no known data for this realm. Sorry :(");
	end
end