
## CSharp

#### Requeriments:
* [System.Web.Extensions.dll](https://msdn.microsoft.com/pt-br/library/system.web.script.serialization.javascriptserializer(v=vs.110).aspx) - JSON Serializing

```csharp
namespace HiRezAPIWrapper {
	class Program {
		public class Session {
			public string ret_msg { get; set; }
			public string session_id { get; set; }
			public string timestamp { get; set; }
			public override string ToString() {
				return string.Format("[Session ret_msg={0}, session_id={1}, timestamp={2}]", this.ret_msg, this.session_id, this.timestamp);
			}
		}
		public class HirezAPI {
			private int dev_id;
			private string auth_key;
			private static string BASE_ENDPOINT = "https://api.realmroyale.com/realmapi.svc";
			private Session session;
			
			public HirezAPI(string dev_id, string auth_key) : this(int.Parse(dev_id), auth_key) { }
			public HirezAPI(int dev_id, string auth_key) {
				this.auth_key = auth_key;
				this.dev_id = dev_id;
			}
			
			public void CreateSession() {
				string url = string.Format("{0}/createsessionjson/{1}/{2}/{3}", BASE_ENDPOINT, this.dev_id, this.GenerateSignature("createsession"), this.GetTimeStamp());
				this.session = this.Deserialize<Session>(this.RequestURL(url));
				System.Console.WriteLine(this.session);
			}
			
			private string RequestURL(string url) {
				if (!string.IsNullOrEmpty(url)) {
					var request = System.Net.WebRequest.Create(url);
					string str = string.Empty;
					using (var response = request.GetResponse()) {
						using (var dataStream = response.GetResponseStream()) {
							using (var reader = new System.IO.StreamReader(dataStream)) {
								str = reader.ReadToEnd();
							}
						}
					}
					return str;
				}
				return url;
			}
			protected T Deserialize<T>(string input) {
				T ret = default(T);
				
				var jss = new System.Web.Script.Serialization.JavaScriptSerializer();

				ret = jss.Deserialize<T>(input);

				return ret;
			}
			
			private static string GetMD5Hash(string input) {
				using(var md5 = System.Security.Cryptography.MD5.Create()) {
					var bytes = md5.ComputeHash(System.Text.Encoding.UTF8.GetBytes(input));
					var string_builder = new System.Text.StringBuilder();
					foreach (byte b in bytes)
						string_builder.Append(b.ToString("x2").ToLower());
					return string_builder.ToString();
				}
			}
			public string GenerateSignature(string method, string timestamp="") {
				if(string.IsNullOrEmpty(method))
					return string.Empty;
				return GetMD5Hash(this.dev_id + method.ToLower() + this.auth_key + (string.IsNullOrEmpty(timestamp) ? this.GetTimeStamp() : timestamp));
			}
			
			public string GetTimeStamp(string format="yyyyMMddHHmmss") {
				return System.DateTime.UtcNow.ToString(format);
			}
		}
		public static void Main(string[] args) {
			HirezAPI hirezAPI = new HirezAPI(1004, "23DF3C7E9BD14D84BF892AD206B6755C");
			hirezAPI.CreateSession();

			System.Console.Write("Press any key to continue . . . ");
			System.Console.ReadKey(true);
		}
	}
}
```
