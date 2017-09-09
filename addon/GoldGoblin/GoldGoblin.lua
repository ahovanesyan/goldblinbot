GoldGoblinData = {};

SLASH_GOLDGOBLIN1, SLASH_GOLDGOBLIN2 = '/gg', '/goldgoblin';

function SlashCmdList.GOLDGOBLIN(msg, editbox)
	if msg == "" then
		getprospectingdata(GetRealmName());
	elseif GoldGoblinData[msg] ~= nil then
		getprospectingdata(msg);
	else
		DEFAULT_CHAT_FRAME:AddMessage("There is no known data for \'" .. msg .. "\'. Sorry :(");
	end	
end

function getprospectingdata(realm)
	if GoldGoblinData[realm] ~= nil then
		DEFAULT_CHAT_FRAME:AddMessage("Prospecting data for |cFFFFFF00" .. realm);
		for k, v in ipairs(GoldGoblinData[realm]) do
			for key, value in pairs(v) do
				DEFAULT_CHAT_FRAME:AddMessage("|cFF00FF00" .. key .. ": |r" .. value);
			end
		end
	else
		DEFAULT_CHAT_FRAME:AddMessage("There is no known data for \'" .. realm .. "\'. Sorry :(");
	end
end