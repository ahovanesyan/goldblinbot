SLASH_GOLDGOBLIN1, SLASH_GOLDGOBLIN2 = '/gg', '/goldgoblin';

function SlashCmdList.GOLDGOBLIN(msg, editbox)
	if msg == "" then
		for k, v in ipairs(GoldGoblinData) do
			for key, value in pairs(v) do
				DEFAULT_CHAT_FRAME:AddMessage("|cFF00FF00" .. key .. ": |r" .. value);
			end
		end
	elseif GoldGoblinData[msg] ~= nil then
		DEFAULT_CHAT_FRAME:AddMessage(GoldGoblinData[msg]);
	else
		DEFAULT_CHAT_FRAME:AddMessage('GoldGoblin did not recognize command \'' .. msg .. '\'');
	end
end