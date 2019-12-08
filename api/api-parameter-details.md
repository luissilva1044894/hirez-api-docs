
# API Parameter Details

## Response Type

The API supports both [JSON][json_website] and XML responses. However, we strongly suggest only using [JSON][json_website] when requesting resources.

## Date
><i>A DateTime formatted to ``yyyyMMdd``</i><br/><br/>Will be like “20180711” - for Jul 11, 2018

date - a string in the format “20171231” (for Dec 31, 2017, as an example)

## Hour

To avoid HTTP timeouts in the [``GetMatchIdsByQueue``](#get-match-ids-by-queue) method, you can now specify a 10-minute window within the specified {hour} field to lessen the size of data returned by appending a “,mm” value to the end of {hour}. For example, to get the match Ids for the first 10 minutes of hour 3, you would specify {hour} as “3,00”.  This would only return the Ids between the time 3:00 to 3:09.  Rules below:
			Only valid values for mm are “00”, “10”, “20”, “30”, “40”, “50”
			To get the entire third hour worth of Match Ids, call [``GetMatchIdsByQueue``](#get-match-ids-by-queue) 6 times, specifying the following values for {hour}: “3,00”, “3,10”, “3,20”, “3,30”, “3,40”, “3,50”. 
			The standard, full hour format of {hour} = “hh” is still supported.

## God ID
> int

The God ID is an unique id for each playable character in a game.

Can be obtained from [``GetGods``](./../get-gods.md#get-gods) & [``GetChampions``](./../get-champions.md#get-champions).

### Paladins

<details markdown="1">
<summary>Champions</summary>

<!-- https://cms.paladins.com/wp-json/api/champion-hub/1 -->
There are currently 44 playable champions (Updated in 12-08-2019):
<table>
	<tr>
		<th>ID</th>
		<th>Name</th>
		<th>Role</th>
		<th>Title</th>
		<th>Image</th>
	</tr>
	<tr>
		<td>2205</td>
		<td>Androxus</td>
		<td>Flank</td>
		<td>The Godslayer</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/androxus.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2404</td>
		<td>Ash</td>
		<td>Front Line</td>
		<td>The War Machine</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/ash.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2512</td>
		<td>Atlas</td>
		<td>Front Line</td>
		<td>The Man Out of Time</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/atlas.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2073</td>
		<td>Barik</td>
		<td>Front Line</td>
		<td>The Master Mechanic</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/barik.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2281</td>
		<td>Bomb King</td>
		<td>Damage</td>
		<td>His Majesty</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/bomb-king.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2147</td>
		<td>Buck</td>
		<td>Flank</td>
		<td>The Unyielding</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/buck.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2092</td>
		<td>Cassie</td>
		<td>Damage</td>
		<td>The Hunter's Daughter</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/cassie.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2495</td>
		<td>Dredge</td>
		<td>Damage</td>
		<td>Admiral of the Abyss</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/dredge.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2277</td>
		<td>Drogoz</td>
		<td>Damage</td>
		<td>The Greedy</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/drogoz.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2094</td>
		<td>Evie</td>
		<td>Flank</td>
		<td>The Winter Witch</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/evie.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2071</td>
		<td>Fernando</td>
		<td>Front Line</td>
		<td>The Self-Appointed Knight</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/fernando.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2491</td>
		<td>Furia</td>
		<td>Support</td>
		<td>Angel of Vengeance</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/furia.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2093</td>
		<td>Grohk</td>
		<td>Support</td>
		<td>The Lightning Orc</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/grohk.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2254</td>
		<td>Grover</td>
		<td>Support</td>
		<td>The Wild</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/grover.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2509</td>
		<td>Imani</td>
		<td>Damage</td>
		<td>The Last Warder</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/imani.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2348</td>
		<td>Inara</td>
		<td>Front Line</td>
		<td>The Stone Warden</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/inara.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2517</td>
		<td>Io</td>
		<td>Support</td>
		<td>The Shattered Goddess</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/io.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2431</td>
		<td>Jenos</td>
		<td>Support</td>
		<td>The Ascended</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/jenos.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2479</td>
		<td>Khan</td>
		<td>Front Line</td>
		<td>Primus of house Aico</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/khan.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2249</td>
		<td>Kinessa</td>
		<td>Damage</td>
		<td>The Bounty Hunter</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/kinessa.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2493</td>
		<td>Koga</td>
		<td>Flank</td>
		<td>The Lost Hand</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/koga.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2362</td>
		<td>Lex</td>
		<td>Flank</td>
		<td>The Hand of Justice</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/lex.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2417</td>
		<td>Lian</td>
		<td>Damage</td>
		<td>Scion of House Aico</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/lian.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2338</td>
		<td>Maeve</td>
		<td>Flank</td>
		<td>of Blades</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/maeve.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2288</td>
		<td>Makoa</td>
		<td>Front Line</td>
		<td>The Ancient</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/makoa.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2303</td>
		<td>Mal'Damba</td>
		<td>Support</td>
		<td>Wekono's Chosen</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/maldamba.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2481</td>
		<td>Moji</td>
		<td>Flank</td>
		<td>and Friends</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/moji.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2056</td>
		<td>Pip</td>
		<td>Support</td>
		<td>The Rogue Alchemist</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/pip.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2528</td>
		<td>Raum</td>
		<td>Front Line</td>
		<td>Rage of the Abyss</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/raum.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2149</td>
		<td>Ruckus</td>
		<td>Front Line</td>
		<td>The Worst of Friends</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/ruckus.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2372</td>
		<td>Seris</td>
		<td>Support</td>
		<td>Oracle of the Abyss</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/seris.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2307</td>
		<td>Sha Lin</td>
		<td>Damage</td>
		<td>The Desert Wind</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/sha-lin.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2057</td>
		<td>Skye</td>
		<td>Flank</td>
		<td>The Twilight Assassin</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/skye.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2438</td>
		<td>Strix</td>
		<td>Damage</td>
		<td>Ghost Feather</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/strix.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2472</td>
		<td>Talus</td>
		<td>Flank</td>
		<td>of the Ska'drin</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/talus.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2477</td>
		<td>Terminus</td>
		<td>Front Line</td>
		<td>The Fallen</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/terminus.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2529</td>
		<td>Tiberius</td>
		<td>Damage</td>
		<td>The Weapons Master</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/tiberius.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2322</td>
		<td>Torvald</td>
		<td>Front Line</td>
		<td>The Runic Sage</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/torvald.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2314</td>
		<td>Tyra</td>
		<td>Damage</td>
		<td>The Untamed</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/tyra.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2285</td>
		<td>Viktor</td>
		<td>Damage</td>
		<td>The Lone Wolf</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/viktor.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2480</td>
		<td>Vivian</td>
		<td>Damage</td>
		<td>The Cunning</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/vivian.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2393</td>
		<td>Willo</td>
		<td>Damage</td>
		<td>of the Summer Court</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/willo.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2267</td>
		<td>Ying</td>
		<td>Support</td>
		<td>The Blossom</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/ying.jpg" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2420</td>
		<td>Zhin</td>
		<td>Flank</td>
		<td>The Tyrant</td>
		<td><img src="https://web2.hirez.com/paladins/champion-icons/zhin.jpg" height="64" width="64"/></td>
	</tr>
</table>

</details>


### Realm Royale

There are multiple Classes in Realm Royale. Each one has its own unique abilities and fighting style.<br/><br/>Each class has a unique passive bonus, movement ability, and 4 special abilities.<br/>Additionally each class can craft a unique weapon at the forge.

<details markdown="1">
<summary>Classes</summary>

There are currently 4 playable classes:
<table>
	<tr>
		<th>ID</th>
		<th>Name</th>
		<th>In-Game Name</th>
		<th>Image</th>
	</tr>
	<tr>
		<td>2285</td>
		<td>Male Tank</td>
		<td>Warrior</td>
		<td><img src="./../_assets/realm-royale/class-warrior.png" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2493</td>
		<td>Female Damage</td>
		<td>Hunter</td>
		<td><img src="./../_assets/realm-royale/class-hunter.png" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2494</td>
		<td>Female Support</td>
		<td>Mage</td>
		<td><img src="./../_assets/realm-royale/class-mage.png" height="64" width="64"/></td>
	</tr>
	<tr>
		<td>2496</td>
		<td>Male Flank</td>
		<td>Assassin</td>
		<td><img src="./../_assets/realm-royale/class-assassin.png" height="64" width="64"/></td>
	</tr>
</table>

</details>

### Smite
<details markdown="1">
<summary>Gods</summary>

<!-- https://cms.smitegame.com/wp-json/smite-api/all-gods/1 -->
<table>
	<tr>
		<th>ID</th>
		<th>Name</th>
		<th>Role</th>
		<th>Title</th>
		<th>Image</th>
	</tr>
	<tr>
		<td>3492</td>
		<td>Achilles</td>
		<td>Warrior</td>
		<td></td>
		<td><img src="https://web2.hirez.com/smite/god-icons/achilles.jpg" height="64" width="64"/></td>
	</tr>
</table>
</details>

## Language
><i>The language Id that you want results returned in. Default is 1.</i>

Valid values:
<table>
	<tr>
		<th>ID</th>
		<th>Language</th>
	</tr>
	<tr>
		<td>1</td>
		<td>English</td>
	</tr>
	<tr>
		<td>2</td>
		<td>German</td>
	</tr>
	<tr>
		<td>3</td>
		<td>French</td>
	</tr>
	<tr>
		<td>5</td>
		<td>Chinese</td>
	</tr>
	<tr>
		<td>7</td>
		<td>Spanish</td>
	</tr>
	<tr>
		<td>9</td>
		<td>Spanish (Latin America)</td>
	</tr>
	<tr>
		<td>10</td>
		<td>Portuguese</td>
	</tr>
	<tr>
		<td>11</td>
		<td>Russian</td>
	</tr>
	<tr>
		<td>12</td>
		<td>Polish</td>
	</tr>
	<tr>
		<td>13</td>
		<td>Turkish</td>
	</tr>
</table>

## Match ID

><i>The id of a match.</i><br/>

The Match ID is an unique id for each map that’s created by the server for a set of players.

Can be obtained from [``GetMatchHistory``](./../get-match-history.md#get-match-history), [``GetMatchIdsByQueue``](./../get-match-ids-by-queue.md#get-match-ids-by-queue), [``GetPlayerMatchHistory``](./../get-player-match-history.md#get-player-match-history), [``GetPlayerMatchHistoryAfterDateTime``](./../get-player-match-history-after-datetim.md#get-player-match-history-after-datetime), [``GetPlayerStatus``](./../get-player-status.md#get-player-status), [``GetPlayerMatchHistoryAfterDateTime``](./../get-player-match-history-after-datetim.md#get-player-match-history-after-datetime) & [``GetTopMatches``](./../get-top-matches.md#get-top-matches).

## Player

This may either be:

### Player Name
> string

This is the Player Name.

### Player ID
> int

The Player ID is an unique id for each player that's is created and internally stored by Hi-Rez.

Can be obtained from [``GetPlayer``](./../get-player.md#get-player) & [``GetTopMatches``](./../get-top-matches.md#get-top-matches).

This is the Player ID. The player_id (available to API developers via the /getplayer API method).

### Portal User Id
The (usually) 3rd-Party identifier for a Portal.  Examples:  Steam ID, PS4 GamerTag, Xbox GamerTag, Switch GamerTag.

### Steam ID
> int

This is the Player Steam ID.

### Gamer Tag
Typically an alphanumeric descriptor of an individual on a [Portal](#portal-id). This value might not be unique depending on [Portal](#portal-id).

## Portal
> int

A “Portal” is a gateway into our games via an identifier.  In the past it would have been synonymous with a hardware platform... but because of gateways such as “Steam” it is more than just a hardware platform.

Represents Platform as follows:
<table>
  <tr>
    <th>ID</th>
    <th>Platform</th>
		<th>Image</th>
  </tr>
  <tr>
  	<td>1</td>
  	<td>Hi-Rez</td>
		<td><img src="./../_assets/logos/hirez.png" height="32" width="32"/></td>
  </tr>
  <tr>
  	<td>5</td>
  	<td>Steam</td>
		<td><img src="./../_assets/logos/steam.png" height="32" width="32"/></td>
  </tr>
  <tr>
  	<td>9</td>
  	<td>PS4</td>
		<td><img src="./../_assets/logos/psn.png" height="32" width="32"/></td>
  </tr>
  <tr>
  	<td>10</td>
  	<td>Xbox</td>
		<td><img src="./../_assets/logos/xbox.png" height="32" width="32"/></td>
  </tr>
  <tr>
  	<td>14</td>
  	<td>Mixer</td>
		<td><img src="./../_assets/logos/mixer.png" height="32" width="32"/></td>
  </tr>
  <tr>
  	<td>22</td>
  	<td>Nintendo Switch</td>
		<td><img src="./../_assets/logos/nintendo-switch-black.png" height="32" width="32"/></td>
  </tr>
  <tr>
  	<td>25</td>
  	<td>Discord</td>
		<td><img src="./../_assets/logos/discord.png" height="32" width="32"/></td>
  </tr>
</table>

## Platform type

Windows = 1
Mac = 2
Xbox_Nintendo = 3
PSN = 4
#9: ????? #10: ?????


## Season
The season of a league. Starts at 1 and increases by 1 for each calendar year.  As of 2017-02-01 we are currently on season 4.

## League Tier

Valid values:
<table>
  <tr>
    <th>ID</th>
    <th>Description</th>
		<th>Image</th>
  </tr>
  <tr>
    <td>0</td>
    <td>Unranked</td>
    <td><img src="./../_assets/paladins/league-tier/0.png" height="32" width="32"/></td>
  </tr>
  <tr>
    <td>1</td>
    <td>Bronze V</td>
    <td><img src="./../_assets/paladins/league-tier/1.png" height="32" width="32"/></td>
  </tr>
  <tr>
    <td>2</td>
    <td>Bronze IV</td>
    <td><img src="./../_assets/paladins/league-tier/2.png" height="32" width="32"/></td>
  </tr>
  <tr>
    <td>3</td>
    <td>Bronze III</td>
    <td><img src="./../_assets/paladins/league-tier/3.png" height="32" width="32"/></td>
  </tr>
  <tr>
    <td>4</td>
    <td>Bronze II</td>
    <td><img src="./../_assets/paladins/league-tier/4.png" height="32" width="32"/></td>
  </tr>
  <tr>
    <td>5</td>
    <td>Bronze I</td>
    <td><img src="./../_assets/paladins/league-tier/5.png" height="32" width="32"/></td>
  </tr>
  <tr>
    <td>6</td>
    <td>Silver V</td>
    <td><img src="./../_assets/paladins/league-tier/6.png" height="32" width="32"/></td>
  </tr>
  <tr>
    <td>7</td>
    <td>Silver IV</td>
    <td><img src="./../_assets/paladins/league-tier/7.png" height="32" width="32"/></td>
  </tr>
  <tr>
    <td>8</td>
    <td>Silver III</td>
    <td><img src="./../_assets/paladins/league-tier/8.png" height="32" width="32"/></td>
  </tr>
  <tr>
    <td>9</td>
    <td>Silver II</td>
    <td><img src="./../_assets/paladins/league-tier/9.png" height="32" width="32"/></td>
  </tr>
  <tr>
    <td>10</td>
    <td>Silver I</td>
    <td><img src="./../_assets/paladins/league-tier/10.png" height="32" width="32"/></td>
  </tr>
  <tr>
    <td>11</td>
    <td>Gold V</td>
    <td><img src="./../_assets/paladins/league-tier/11.png" height="32" width="32"/></td>
  </tr>
  <tr>
    <td>12</td>
    <td>Gold IV</td>
    <td><img src="./../_assets/paladins/league-tier/12.png" height="32" width="32"/></td>
  </tr>
  <tr>
    <td>13</td>
    <td>Gold III</td>
    <td><img src="./../_assets/paladins/league-tier/13.png" height="32" width="32"/></td>
  </tr>
  <tr>
    <td>14</td>
    <td>Gold II</td>
    <td><img src="./../_assets/paladins/league-tier/14.png" height="32" width="32"/></td>
  </tr>
  <tr>
    <td>15</td>
    <td>Gold I</td>
    <td><img src="./../_assets/paladins/league-tier/15.png" height="32" width="32"/></td>
  </tr>
  <tr>
    <td>16</td>
    <td>Platinum V</td>
    <td><img src="./../_assets/paladins/league-tier/16.png" height="32" width="32"/></td>
  </tr>
  <tr>
    <td>17</td>
    <td>Platinum IV</td>
    <td><img src="./../_assets/paladins/league-tier/17.png" height="32" width="32"/></td>
  </tr>
  <tr>
    <td>18</td>
    <td>Platinum III</td>
    <td><img src="./../_assets/paladins/league-tier/18.png" height="32" width="32"/></td>
  </tr>
  <tr>
    <td>19</td>
    <td>Platinum II</td>
    <td><img src="./../_assets/paladins/league-tier/19.png" height="32" width="32"/></td>
  </tr>
  <tr>
    <td>20</td>
    <td>Platinum I</td>
    <td><img src="./../_assets/paladins/league-tier/20.png" height="32" width="32"/></td>
  </tr>
  <tr>
    <td>21</td>
    <td>Diamond V</td>
    <td><img src="./../_assets/paladins/league-tier/21.png" height="32" width="32"/></td>
  </tr>
  <tr>
    <td>22</td>
    <td>Diamond IV</td>
    <td><img src="./../_assets/paladins/league-tier/22.png" height="32" width="32"/></td>
  </tr>
  <tr>
    <td>23</td>
    <td>Diamond III</td>
    <td><img src="./../_assets/paladins/league-tier/23.png" height="32" width="32"/></td>
  </tr>
  <tr>
    <td>24</td>
    <td>Diamond II</td>
    <td><img src="./../_assets/paladins/league-tier/24.png" height="32" width="32"/></td>
  </tr>
  <tr>
    <td>25</td>
    <td>Diamond I</td>
    <td><img src="./../_assets/paladins/league-tier/25.png" height="32" width="32"/></td>
  </tr>
  <tr>
    <td>26</td>
    <td>Master</td>
    <td><img src="./../_assets/paladins/league-tier/26.png" height="32" width="32"/></td>
  </tr>
  <tr>
    <td>27</td>
    <td>Grandmaster</td>
    <td><img src="./../_assets/paladins/league-tier/27.png" height="32" width="32"/></td>
  </tr>
</table>


## Status

Represents Player Status as follows:
<table>
  <tr>
    <th>ID</th>
    <th>Type</th>
    <th>Description</th>
  </tr>
  <tr>
  	<td>0</td>
  	<td>Offline</td>
  	<td></td>
  </tr>
  <tr>
  	<td>1</td>
  	<td>In Lobby</td>
  	<td>Basically anywhere except god selection or in game.</td>
  </tr>
  <tr>
  	<td>2</td>
  	<td>God Selection</td>
  	<td>Player has accepted match and is selecting god before start of game.</td>
  </tr>
  <tr>
  	<td>3</td>
  	<td>In Game</td>
  	<td>Match has started.</td>
  </tr>
  <tr>
  	<td>4</td>
  	<td>Online</td>
  	<td>Player is logged in, but may be blocking broadcast of player state.</td>
  </tr>
  <tr>
  	<td>5</td>
  	<td>Unknown</td>
  	<td>Player not found.</td>
  </tr>
</table>


## Signature
><i>A MD5 hash of (dev_id + method + auth_key + [Timestamp](#timestamp.md))</i>

A distinct signature is required for each API method called.

Actually the auth_key isn't passed directly, but instead embedded and hashed in another parameter (Signature).

The Signature is created by concatenating several fields and then hashing the result with an MD5 algorithm. The components of this hash are (in order):
- dev_id
- Method
  - Which “method” means the resource you want to retrieve data (eg, “createsession”)
  <!-- The method name being called -->
  - This will not include the ResponseType, just the name of the method.
- auth_key
- Current UTC [**Timestamp**](https://github.com/luissilva1044894/PaladinsAPI-demo/blob/master/getting-started/Timestamp.md)

<details>
 <summary>C# Sample</summary>

```csharp
private static string GetMD5Hash(string input) {
  using (var md5 = System.Security.Cryptography.MD5.Create()) {
    var bytes = md5.ComputeHash(System.Text.Encoding.UTF8.GetBytes(input));
    var stringBuilder = new System.Text.StringBuilder();
    foreach (byte b in bytes)
      stringBuilder.Append(b.ToString("x2").ToLower());
    return stringBuilder.ToString();
  }
}
public string generateSignature(int devId, string method, string authKey, string timestamp) {
  return GetMD5Hash(devKey + method + authKey + timestamp);
}
var signature = generateSignature(1004, "createsession", "23DF3C7E9BD14D84BF892AD206B6755C", getTimestamp());
```
</details>

<details>
 <summary>Java Sample</summary>

```java
private static String generateSignature(int devId, String authKey, String method, String timestamp) {
  String templateSignature = devId + method + authKey + timestamp;
  StringBuilder signatureBuilder = new StringBuilder();
  try {
    MessageDigest md = MessageDigest.getInstance("MD5");
    md.update (templateSignature.getBytes());
    byte [] bytes = md.digest();

    for (byte b : bytes) {
      String hex = Integer.toHexString(0xff & b);
      if (hex.length () == 1)
        signatureBuilder.append("0");
      signatureBuilder.append(hex);
    }
  } catch (NoSuchAlgorithmException e) {
    e.printStackTrace();
  }

  return signatureBuilder.toString();
}

public final String signature = generateSignature(1004, "createsession", "23DF3C7E9BD14D84BF892AD206B6755C", getTimestamp());
```
</details>

<details>
 <summary>Javascript Sample</summary>

```js
const md5 = require("md5");
function generateSignature(devId, method, authKey, timestamp) {
  return md5(`${devId}${method}${apiKey}${timestamp}`);
}
var signature = generateSignature(1004, "createsession", "23DF3C7E9BD14D84BF892AD206B6755C", getTimestamp());
```
</details>

<details>
 <summary>PHP Sample</summary>

```php
private function getSignature($devId, $method, $authKey, $timestamp) {
    return md5($devId . $method . $authKey . $timestamp);
}
```
</details>

<details>
 <summary>Python Sample</summary>

```python
from hashlib import md5 as GetMD5Hash
def __encode__(_input, encodeType="utf-8"):
  return str(_input).encode(encodeType)
def generateSignature(devId, method, authKey, timestamp):
  return GetMD5Hash(__encode__("{0}{1}{2}{3}".format(devId, method, authKey, timestamp)).hexdigest()
signature = generateSignature(1004, "createsession", "23DF3C7E9BD14D84BF892AD206B6755C", getTimestamp());
```
</details>


## Timestamp
><i>Current UTC time (GMT+0) formatted to '**``YYYYMMDDHHmmss``**'.</i>

**Timestamps** are used by [**Signatures**](#signatures.md) and embedded into URLs when sending requests, they have to be formatted properly to ensure the request completes without error.

<details>
 <summary>C# Sample</summary>

```csharp
public static string getTimestamp(string tmFormat="yyyyMMddHHmmss") {
  return System.DateTime.UtcNow.ToString(tmFormat);
}
var timestamp = getTimeStamp();
```
</details>

<details>
 <summary>Java Sample</summary>

```java
private static String getTimestamp() {
  SimpleDateFormat sdf = new SimpleDateFormat("yyyyMMddHHmmss");
  sdf.setTimeZone(new SimpleTimeZone(SimpleTimeZone.UTC_TIME, "UTC"));
  return sdf.format(new Date());
}
public final String timestamp = getTimestamp();
```
</details>


<details>
 <summary>Javascript Sample</summary>

```js
const moment = require("moment");
function getTimestamp() {
  return moment.utc().format("YYYYMMDDHHmmss");
}
var timestamp = getTimeStamp();
```
</details>

<details>
 <summary>PHP Sample</summary>

```php
private function getTimestamp() {
  return Carbon::now()->format('Ymdhis');
}
```
</details>

<details>
 <summary>Python Sample</summary>

```Python
def getTimestamp(tmFormat="%Y%m%d%H%M%S"):
  from datetime import datetime
  return datetime.utcnow().strftime(tmFormat)
timeStamp = getTimeStamp()
```
</details>

[json_website]: https://json.org/ "Visit json.org"
