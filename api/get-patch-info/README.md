`GET` `/GetPatchInfo[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}`

## Get Patch Info
><i>/**GetPatchInfo**[ResponseFormat]/{devID}/{signature}/{session}/{timestamp}</i><br/>Returns information about current deployed patch.<br/><br/>CURRENTLY, THIS INFORMATION ONLY INCLUDES PATCH VERSION.

<table>
	<tr>
		<th>Parameter</th>
		<th>Description</th>
		<th>Example</th>
	</tr>
	<tr>
		<td>ResponseFormat</td>
		<td>JSON or XML</td>
		<td>json</td>
	</tr>
	<tr>
		<td>devID</td>
		<td>The devID from your <a href="https://github.com/apugh/realm-api-proposal/wiki/Getting-Started#credentials" title="Credentials">Credentials</a></td>
		<td>1004</td>
	</tr>
	<tr>
		<td>signature</td>
		<td>The <a href="https://github.com/apugh/realm-api-proposal/wiki/Getting-Started#signature" title="Signature">Signature</a> of <b>“GetPatchInfo”</b> method</td>
		<td>a4b47cbe1a5f9488c2ba760c50f30cf1 </td>
	</tr>
	<tr>
		<td>session</td>
		<td>A valid <a href="https://github.com/apugh/realm-api-proposal/wiki/Getting-Started#sessions">Session</a></td>
		<td>1465AFCA32DBDB800CEF8C72F296C52C</td>
	</tr>
	<tr>
		<td>timestamp</td>
		<td>The current <a href="https://github.com/apugh/realm-api-proposal/wiki/Getting-Started#timestamp" title="Timestamp">Timestamp</a></td>
		<td>20180628012612</td>
	</tr>
</table>

<br/><br/>
**Requesting JSON**: http://api.realmroyale.com/realmapi.svc/GetPatchInfoJSON/1004/a4b47cbe1a5f9488c2ba760c50f30cf1/1465AFCA32DBDB800CEF8C72F296C52C/20180628012612

**Response**: JSON
``` json
{
	"version": "0.4.232.2",
	"version_id": 262376,
	"version_code":  "OB4",
	"ret_msg": null
}
```
***
