/*
 * clearconsensus-sdk
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;

import java.lang.reflect.Type;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;

import org.openapitools.client.JSON;

/**
 * TitaniumEvpStatus
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-11-17T19:20:46.452236Z[UTC]")
public class TitaniumEvpStatus {
  public static final String SERIALIZED_NAME_ADDED = "added";
  @SerializedName(SERIALIZED_NAME_ADDED)
  private String added;

  public static final String SERIALIZED_NAME_ASSET = "asset";
  @SerializedName(SERIALIZED_NAME_ASSET)
  private String asset;

  public static final String SERIALIZED_NAME_DATE = "date";
  @SerializedName(SERIALIZED_NAME_DATE)
  private String date;

  public static final String SERIALIZED_NAME_DEALER = "dealer";
  @SerializedName(SERIALIZED_NAME_DEALER)
  private String dealer;

  public static final String SERIALIZED_NAME_INSTRUMENT_TYPE = "instrumentType";
  @SerializedName(SERIALIZED_NAME_INSTRUMENT_TYPE)
  private String instrumentType;

  public static final String SERIALIZED_NAME_LOG_PATH = "logPath";
  @SerializedName(SERIALIZED_NAME_LOG_PATH)
  private String logPath;

  public static final String SERIALIZED_NAME_S3PATH = "s3path";
  @SerializedName(SERIALIZED_NAME_S3PATH)
  private String s3path;

  public static final String SERIALIZED_NAME_SNAP_TIME = "snapTime";
  @SerializedName(SERIALIZED_NAME_SNAP_TIME)
  private String snapTime;

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private String status;

  public static final String SERIALIZED_NAME_USER_EMAIL = "userEmail";
  @SerializedName(SERIALIZED_NAME_USER_EMAIL)
  private String userEmail;

  public TitaniumEvpStatus() { 
  }

  public TitaniumEvpStatus added(String added) {
    
    this.added = added;
    return this;
  }

   /**
   * Get added
   * @return added
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getAdded() {
    return added;
  }


  public void setAdded(String added) {
    this.added = added;
  }


  public TitaniumEvpStatus asset(String asset) {
    
    this.asset = asset;
    return this;
  }

   /**
   * Get asset
   * @return asset
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getAsset() {
    return asset;
  }


  public void setAsset(String asset) {
    this.asset = asset;
  }


  public TitaniumEvpStatus date(String date) {
    
    this.date = date;
    return this;
  }

   /**
   * Get date
   * @return date
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getDate() {
    return date;
  }


  public void setDate(String date) {
    this.date = date;
  }


  public TitaniumEvpStatus dealer(String dealer) {
    
    this.dealer = dealer;
    return this;
  }

   /**
   * Get dealer
   * @return dealer
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getDealer() {
    return dealer;
  }


  public void setDealer(String dealer) {
    this.dealer = dealer;
  }


  public TitaniumEvpStatus instrumentType(String instrumentType) {
    
    this.instrumentType = instrumentType;
    return this;
  }

   /**
   * Get instrumentType
   * @return instrumentType
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getInstrumentType() {
    return instrumentType;
  }


  public void setInstrumentType(String instrumentType) {
    this.instrumentType = instrumentType;
  }


  public TitaniumEvpStatus logPath(String logPath) {
    
    this.logPath = logPath;
    return this;
  }

   /**
   * Get logPath
   * @return logPath
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getLogPath() {
    return logPath;
  }


  public void setLogPath(String logPath) {
    this.logPath = logPath;
  }


  public TitaniumEvpStatus s3path(String s3path) {
    
    this.s3path = s3path;
    return this;
  }

   /**
   * Get s3path
   * @return s3path
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getS3path() {
    return s3path;
  }


  public void setS3path(String s3path) {
    this.s3path = s3path;
  }


  public TitaniumEvpStatus snapTime(String snapTime) {
    
    this.snapTime = snapTime;
    return this;
  }

   /**
   * Get snapTime
   * @return snapTime
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getSnapTime() {
    return snapTime;
  }


  public void setSnapTime(String snapTime) {
    this.snapTime = snapTime;
  }


  public TitaniumEvpStatus status(String status) {
    
    this.status = status;
    return this;
  }

   /**
   * Get status
   * @return status
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getStatus() {
    return status;
  }


  public void setStatus(String status) {
    this.status = status;
  }


  public TitaniumEvpStatus userEmail(String userEmail) {
    
    this.userEmail = userEmail;
    return this;
  }

   /**
   * Get userEmail
   * @return userEmail
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getUserEmail() {
    return userEmail;
  }


  public void setUserEmail(String userEmail) {
    this.userEmail = userEmail;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumEvpStatus titaniumEvpStatus = (TitaniumEvpStatus) o;
    return Objects.equals(this.added, titaniumEvpStatus.added) &&
        Objects.equals(this.asset, titaniumEvpStatus.asset) &&
        Objects.equals(this.date, titaniumEvpStatus.date) &&
        Objects.equals(this.dealer, titaniumEvpStatus.dealer) &&
        Objects.equals(this.instrumentType, titaniumEvpStatus.instrumentType) &&
        Objects.equals(this.logPath, titaniumEvpStatus.logPath) &&
        Objects.equals(this.s3path, titaniumEvpStatus.s3path) &&
        Objects.equals(this.snapTime, titaniumEvpStatus.snapTime) &&
        Objects.equals(this.status, titaniumEvpStatus.status) &&
        Objects.equals(this.userEmail, titaniumEvpStatus.userEmail);
  }

  @Override
  public int hashCode() {
    return Objects.hash(added, asset, date, dealer, instrumentType, logPath, s3path, snapTime, status, userEmail);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumEvpStatus {\n");
    sb.append("    added: ").append(toIndentedString(added)).append("\n");
    sb.append("    asset: ").append(toIndentedString(asset)).append("\n");
    sb.append("    date: ").append(toIndentedString(date)).append("\n");
    sb.append("    dealer: ").append(toIndentedString(dealer)).append("\n");
    sb.append("    instrumentType: ").append(toIndentedString(instrumentType)).append("\n");
    sb.append("    logPath: ").append(toIndentedString(logPath)).append("\n");
    sb.append("    s3path: ").append(toIndentedString(s3path)).append("\n");
    sb.append("    snapTime: ").append(toIndentedString(snapTime)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    userEmail: ").append(toIndentedString(userEmail)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("added");
    openapiFields.add("asset");
    openapiFields.add("date");
    openapiFields.add("dealer");
    openapiFields.add("instrumentType");
    openapiFields.add("logPath");
    openapiFields.add("s3path");
    openapiFields.add("snapTime");
    openapiFields.add("status");
    openapiFields.add("userEmail");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumEvpStatus
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumEvpStatus.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumEvpStatus is not found in the empty JSON string", TitaniumEvpStatus.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumEvpStatus.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumEvpStatus` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      if (jsonObj.get("added") != null && !jsonObj.get("added").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `added` to be a primitive type in the JSON string but got `%s`", jsonObj.get("added").toString()));
      }
      if (jsonObj.get("asset") != null && !jsonObj.get("asset").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `asset` to be a primitive type in the JSON string but got `%s`", jsonObj.get("asset").toString()));
      }
      if (jsonObj.get("date") != null && !jsonObj.get("date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("date").toString()));
      }
      if (jsonObj.get("dealer") != null && !jsonObj.get("dealer").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `dealer` to be a primitive type in the JSON string but got `%s`", jsonObj.get("dealer").toString()));
      }
      if (jsonObj.get("instrumentType") != null && !jsonObj.get("instrumentType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `instrumentType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("instrumentType").toString()));
      }
      if (jsonObj.get("logPath") != null && !jsonObj.get("logPath").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `logPath` to be a primitive type in the JSON string but got `%s`", jsonObj.get("logPath").toString()));
      }
      if (jsonObj.get("s3path") != null && !jsonObj.get("s3path").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `s3path` to be a primitive type in the JSON string but got `%s`", jsonObj.get("s3path").toString()));
      }
      if (jsonObj.get("snapTime") != null && !jsonObj.get("snapTime").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `snapTime` to be a primitive type in the JSON string but got `%s`", jsonObj.get("snapTime").toString()));
      }
      if (jsonObj.get("status") != null && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      if (jsonObj.get("userEmail") != null && !jsonObj.get("userEmail").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `userEmail` to be a primitive type in the JSON string but got `%s`", jsonObj.get("userEmail").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumEvpStatus.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumEvpStatus' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumEvpStatus> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumEvpStatus.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumEvpStatus>() {
           @Override
           public void write(JsonWriter out, TitaniumEvpStatus value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumEvpStatus read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumEvpStatus given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumEvpStatus
  * @throws IOException if the JSON string is invalid with respect to TitaniumEvpStatus
  */
  public static TitaniumEvpStatus fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumEvpStatus.class);
  }

 /**
  * Convert an instance of TitaniumEvpStatus to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

