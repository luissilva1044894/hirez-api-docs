
## Java

#### Requeriments:
* [OkHttp3](https://search.maven.org/search?q=g:com.squareup.okhttp3%20AND%20a:okhttp) - Http Client
* [Jackson Databind](https://search.maven.org/search?q=g:com.fasterxml.jackson.core%20AND%20a:jackson-databind) - JSON Serializing
* [Project Lombok](https://search.maven.org/search?q=g:org.projectlombok%20AND%20a:lombok) - for annotation processing

```java
import com.fasterxml.jackson.core.JsonGenerator;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.PropertyNamingStrategy;
import lombok.Data;
import lombok.Getter;
import lombok.Setter;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

import java.io.IOException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.text.SimpleDateFormat;
import java.util.Arrays;
import java.util.Date;
import java.util.SimpleTimeZone;
import java.util.stream.Collectors;

class Program {
	@Data
	public static class Session {
		private String retMsg;
		private String sessionId;
		private String timestamp;
	}

	public static class RealmAPI {
		private static final String BASE_ENDPOINT = "http://api.realmroyale.com/realmapi.svc";

		private final Integer devId;
		private final String authKey;

		@Getter
		@Setter
		private Session currentSession;

		private final ObjectMapper mapper = new ObjectMapper();
		private final OkHttpClient httpClient = new OkHttpClient();

		public RealmAPI(String devId, String authKey) {
			this(Integer.parseInt(devId), authKey);
		}

		public RealmAPI(Integer devId, String authKey) {
			this.devId = devId;
			this.authKey = authKey;

			this.mapper.disable(JsonGenerator.Feature.IGNORE_UNKNOWN);
			this.mapper.setPropertyNamingStrategy(PropertyNamingStrategy.SNAKE_CASE);
		}

		public RealmAPI buildSession() {
			try {
				setCurrentSession(exchange("createsession", Session.class));
			} catch (IOException e) {
				e.printStackTrace();
			}
			return this;
		}

		private <T> T exchange(String method, Class<T> responseType, String... params) throws IOException {
			String signature = generateSignature(method) + ((currentSession != null && !method.equalsIgnoreCase("createsession")) ? currentSession.getSessionId() : "");
			String uri = String.format("%s/%s/%s/%s",
					BASE_ENDPOINT, method + "json", signature, getTimestamp());

			if (params.length > 0) {
				uri += '/' + Arrays.stream(params).collect(Collectors.joining("/"));
			}
			Response response = httpClient.newCall(new Request.Builder().get().url(uri).build()).execute()
			return mapper.readValue(response.body().bytes(), responseType);
		}

		private String generateSignature(String method) {
			String templateSignature = devId + method + authKey + getTimestamp();
			StringBuilder signatureBuilder = new StringBuilder();
			try {
				MessageDigest md = MessageDigest.getInstance("MD5");
				md.update(templateSignature.getBytes());
				byte[] bytes = md.digest();

				for (byte b : bytes) {
					String hex = Integer.toHexString(0xff & b);
					if (hex.length() == 1) {
						signatureBuilder.append("0");
					}
					signatureBuilder.append(hex);
				}
			} catch (NoSuchAlgorithmException e) {
				e.printStackTrace();
			}

			return signatureBuilder.toString();
		}

		private String getTimestamp() {
			SimpleDateFormat sdf = new SimpleDateFormat("yyyyMMddHHmmss");
			sdf.setTimeZone(new SimpleTimeZone(SimpleTimeZone.UTC_TIME, "UTC"));
			return sdf.format(new Date());
		}
	}

	public static void main(String[] args) {
		RealmAPI realmAPI = new RealmAPI(1004, "23DF3C7E9BD14D84BF892AD206B6755C")
				.buildSession();

		System.out.println(realmAPI.getCurrentSession());
	}
}
```
