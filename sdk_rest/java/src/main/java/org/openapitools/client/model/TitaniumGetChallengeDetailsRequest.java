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
 * TitaniumGetChallengeDetailsRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-07-17T19:07:41.695571Z[UTC]")
public class TitaniumGetChallengeDetailsRequest {
  public static final String SERIALIZED_NAME_ASSET_ID = "assetId";
  @SerializedName(SERIALIZED_NAME_ASSET_ID)
  private String assetId;

  public static final String SERIALIZED_NAME_CONSENSUS_RUN_ID = "consensusRunId";
  @SerializedName(SERIALIZED_NAME_CONSENSUS_RUN_ID)
  private String consensusRunId;

  public static final String SERIALIZED_NAME_SUBMISSION_ID = "submissionId";
  @SerializedName(SERIALIZED_NAME_SUBMISSION_ID)
  private String submissionId;

  public static final String SERIALIZED_NAME_SUBMITTED_DATE = "submittedDate";
  @SerializedName(SERIALIZED_NAME_SUBMITTED_DATE)
  private String submittedDate;

  public static final String SERIALIZED_NAME_TRACE_NAME = "traceName";
  @SerializedName(SERIALIZED_NAME_TRACE_NAME)
  private String traceName;

  public TitaniumGetChallengeDetailsRequest() { 
  }

  public TitaniumGetChallengeDetailsRequest assetId(String assetId) {
    
    this.assetId = assetId;
    return this;
  }

   /**
   * Get assetId
   * @return assetId
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getAssetId() {
    return assetId;
  }


  public void setAssetId(String assetId) {
    this.assetId = assetId;
  }


  public TitaniumGetChallengeDetailsRequest consensusRunId(String consensusRunId) {
    
    this.consensusRunId = consensusRunId;
    return this;
  }

   /**
   * Get consensusRunId
   * @return consensusRunId
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getConsensusRunId() {
    return consensusRunId;
  }


  public void setConsensusRunId(String consensusRunId) {
    this.consensusRunId = consensusRunId;
  }


  public TitaniumGetChallengeDetailsRequest submissionId(String submissionId) {
    
    this.submissionId = submissionId;
    return this;
  }

   /**
   * Get submissionId
   * @return submissionId
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getSubmissionId() {
    return submissionId;
  }


  public void setSubmissionId(String submissionId) {
    this.submissionId = submissionId;
  }


  public TitaniumGetChallengeDetailsRequest submittedDate(String submittedDate) {
    
    this.submittedDate = submittedDate;
    return this;
  }

   /**
   * Get submittedDate
   * @return submittedDate
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getSubmittedDate() {
    return submittedDate;
  }


  public void setSubmittedDate(String submittedDate) {
    this.submittedDate = submittedDate;
  }


  public TitaniumGetChallengeDetailsRequest traceName(String traceName) {
    
    this.traceName = traceName;
    return this;
  }

   /**
   * Get traceName
   * @return traceName
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getTraceName() {
    return traceName;
  }


  public void setTraceName(String traceName) {
    this.traceName = traceName;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumGetChallengeDetailsRequest titaniumGetChallengeDetailsRequest = (TitaniumGetChallengeDetailsRequest) o;
    return Objects.equals(this.assetId, titaniumGetChallengeDetailsRequest.assetId) &&
        Objects.equals(this.consensusRunId, titaniumGetChallengeDetailsRequest.consensusRunId) &&
        Objects.equals(this.submissionId, titaniumGetChallengeDetailsRequest.submissionId) &&
        Objects.equals(this.submittedDate, titaniumGetChallengeDetailsRequest.submittedDate) &&
        Objects.equals(this.traceName, titaniumGetChallengeDetailsRequest.traceName);
  }

  @Override
  public int hashCode() {
    return Objects.hash(assetId, consensusRunId, submissionId, submittedDate, traceName);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumGetChallengeDetailsRequest {\n");
    sb.append("    assetId: ").append(toIndentedString(assetId)).append("\n");
    sb.append("    consensusRunId: ").append(toIndentedString(consensusRunId)).append("\n");
    sb.append("    submissionId: ").append(toIndentedString(submissionId)).append("\n");
    sb.append("    submittedDate: ").append(toIndentedString(submittedDate)).append("\n");
    sb.append("    traceName: ").append(toIndentedString(traceName)).append("\n");
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
    openapiFields.add("assetId");
    openapiFields.add("consensusRunId");
    openapiFields.add("submissionId");
    openapiFields.add("submittedDate");
    openapiFields.add("traceName");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumGetChallengeDetailsRequest
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumGetChallengeDetailsRequest.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumGetChallengeDetailsRequest is not found in the empty JSON string", TitaniumGetChallengeDetailsRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumGetChallengeDetailsRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumGetChallengeDetailsRequest` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      if (jsonObj.get("assetId") != null && !jsonObj.get("assetId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `assetId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("assetId").toString()));
      }
      if (jsonObj.get("consensusRunId") != null && !jsonObj.get("consensusRunId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `consensusRunId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("consensusRunId").toString()));
      }
      if (jsonObj.get("submissionId") != null && !jsonObj.get("submissionId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `submissionId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("submissionId").toString()));
      }
      if (jsonObj.get("submittedDate") != null && !jsonObj.get("submittedDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `submittedDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("submittedDate").toString()));
      }
      if (jsonObj.get("traceName") != null && !jsonObj.get("traceName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `traceName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("traceName").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumGetChallengeDetailsRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumGetChallengeDetailsRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumGetChallengeDetailsRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumGetChallengeDetailsRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumGetChallengeDetailsRequest>() {
           @Override
           public void write(JsonWriter out, TitaniumGetChallengeDetailsRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumGetChallengeDetailsRequest read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumGetChallengeDetailsRequest given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumGetChallengeDetailsRequest
  * @throws IOException if the JSON string is invalid with respect to TitaniumGetChallengeDetailsRequest
  */
  public static TitaniumGetChallengeDetailsRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumGetChallengeDetailsRequest.class);
  }

 /**
  * Convert an instance of TitaniumGetChallengeDetailsRequest to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

