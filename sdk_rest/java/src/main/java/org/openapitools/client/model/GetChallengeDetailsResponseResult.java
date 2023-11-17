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
import java.util.ArrayList;
import java.util.List;
import org.openapitools.client.model.GetChallengeDetailsResponseCommonChallengeData;
import org.openapitools.client.model.TitaniumAttachment;

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
 * GetChallengeDetailsResponseResult
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-11-17T19:09:57.005509Z[UTC]")
public class GetChallengeDetailsResponseResult {
  public static final String SERIALIZED_NAME_ATTACHMENTS = "attachments";
  @SerializedName(SERIALIZED_NAME_ATTACHMENTS)
  private List<TitaniumAttachment> attachments = null;

  public static final String SERIALIZED_NAME_CHALLENGE_DATA = "challengeData";
  @SerializedName(SERIALIZED_NAME_CHALLENGE_DATA)
  private Object challengeData;

  public static final String SERIALIZED_NAME_COMMON_CHALLENGE_DATA = "commonChallengeData";
  @SerializedName(SERIALIZED_NAME_COMMON_CHALLENGE_DATA)
  private GetChallengeDetailsResponseCommonChallengeData commonChallengeData;

  public static final String SERIALIZED_NAME_TOTAL_NUMBER = "totalNumber";
  @SerializedName(SERIALIZED_NAME_TOTAL_NUMBER)
  private Object totalNumber;

  public GetChallengeDetailsResponseResult() { 
  }

  public GetChallengeDetailsResponseResult attachments(List<TitaniumAttachment> attachments) {
    
    this.attachments = attachments;
    return this;
  }

  public GetChallengeDetailsResponseResult addAttachmentsItem(TitaniumAttachment attachmentsItem) {
    if (this.attachments == null) {
      this.attachments = new ArrayList<>();
    }
    this.attachments.add(attachmentsItem);
    return this;
  }

   /**
   * Get attachments
   * @return attachments
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<TitaniumAttachment> getAttachments() {
    return attachments;
  }


  public void setAttachments(List<TitaniumAttachment> attachments) {
    this.attachments = attachments;
  }


  public GetChallengeDetailsResponseResult challengeData(Object challengeData) {
    
    this.challengeData = challengeData;
    return this;
  }

   /**
   * Get challengeData
   * @return challengeData
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getChallengeData() {
    return challengeData;
  }


  public void setChallengeData(Object challengeData) {
    this.challengeData = challengeData;
  }


  public GetChallengeDetailsResponseResult commonChallengeData(GetChallengeDetailsResponseCommonChallengeData commonChallengeData) {
    
    this.commonChallengeData = commonChallengeData;
    return this;
  }

   /**
   * Get commonChallengeData
   * @return commonChallengeData
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public GetChallengeDetailsResponseCommonChallengeData getCommonChallengeData() {
    return commonChallengeData;
  }


  public void setCommonChallengeData(GetChallengeDetailsResponseCommonChallengeData commonChallengeData) {
    this.commonChallengeData = commonChallengeData;
  }


  public GetChallengeDetailsResponseResult totalNumber(Object totalNumber) {
    
    this.totalNumber = totalNumber;
    return this;
  }

   /**
   * Get totalNumber
   * @return totalNumber
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getTotalNumber() {
    return totalNumber;
  }


  public void setTotalNumber(Object totalNumber) {
    this.totalNumber = totalNumber;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetChallengeDetailsResponseResult getChallengeDetailsResponseResult = (GetChallengeDetailsResponseResult) o;
    return Objects.equals(this.attachments, getChallengeDetailsResponseResult.attachments) &&
        Objects.equals(this.challengeData, getChallengeDetailsResponseResult.challengeData) &&
        Objects.equals(this.commonChallengeData, getChallengeDetailsResponseResult.commonChallengeData) &&
        Objects.equals(this.totalNumber, getChallengeDetailsResponseResult.totalNumber);
  }

  @Override
  public int hashCode() {
    return Objects.hash(attachments, challengeData, commonChallengeData, totalNumber);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetChallengeDetailsResponseResult {\n");
    sb.append("    attachments: ").append(toIndentedString(attachments)).append("\n");
    sb.append("    challengeData: ").append(toIndentedString(challengeData)).append("\n");
    sb.append("    commonChallengeData: ").append(toIndentedString(commonChallengeData)).append("\n");
    sb.append("    totalNumber: ").append(toIndentedString(totalNumber)).append("\n");
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
    openapiFields.add("attachments");
    openapiFields.add("challengeData");
    openapiFields.add("commonChallengeData");
    openapiFields.add("totalNumber");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to GetChallengeDetailsResponseResult
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (GetChallengeDetailsResponseResult.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetChallengeDetailsResponseResult is not found in the empty JSON string", GetChallengeDetailsResponseResult.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!GetChallengeDetailsResponseResult.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetChallengeDetailsResponseResult` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      JsonArray jsonArrayattachments = jsonObj.getAsJsonArray("attachments");
      if (jsonArrayattachments != null) {
        // ensure the json data is an array
        if (!jsonObj.get("attachments").isJsonArray()) {
          throw new IllegalArgumentException(String.format("Expected the field `attachments` to be an array in the JSON string but got `%s`", jsonObj.get("attachments").toString()));
        }

        // validate the optional field `attachments` (array)
        for (int i = 0; i < jsonArrayattachments.size(); i++) {
          TitaniumAttachment.validateJsonObject(jsonArrayattachments.get(i).getAsJsonObject());
        };
      }
      // validate the optional field `commonChallengeData`
      if (jsonObj.getAsJsonObject("commonChallengeData") != null) {
        GetChallengeDetailsResponseCommonChallengeData.validateJsonObject(jsonObj.getAsJsonObject("commonChallengeData"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetChallengeDetailsResponseResult.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetChallengeDetailsResponseResult' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetChallengeDetailsResponseResult> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetChallengeDetailsResponseResult.class));

       return (TypeAdapter<T>) new TypeAdapter<GetChallengeDetailsResponseResult>() {
           @Override
           public void write(JsonWriter out, GetChallengeDetailsResponseResult value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetChallengeDetailsResponseResult read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of GetChallengeDetailsResponseResult given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of GetChallengeDetailsResponseResult
  * @throws IOException if the JSON string is invalid with respect to GetChallengeDetailsResponseResult
  */
  public static GetChallengeDetailsResponseResult fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetChallengeDetailsResponseResult.class);
  }

 /**
  * Convert an instance of GetChallengeDetailsResponseResult to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

