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
 * TitaniumAllParticipantExplorerTableColumn
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-05-19T17:43:33.578505Z[UTC]")
public class TitaniumAllParticipantExplorerTableColumn {
  public static final String SERIALIZED_NAME_ABS_DIFF_FROM_CONSENSUS_PRICE = "absDiffFromConsensusPrice";
  @SerializedName(SERIALIZED_NAME_ABS_DIFF_FROM_CONSENSUS_PRICE)
  private Object absDiffFromConsensusPrice;

  public static final String SERIALIZED_NAME_CONSENSUS_PRICE = "consensusPrice";
  @SerializedName(SERIALIZED_NAME_CONSENSUS_PRICE)
  private Object consensusPrice;

  public static final String SERIALIZED_NAME_LOWER_BOUNDARY = "lowerBoundary";
  @SerializedName(SERIALIZED_NAME_LOWER_BOUNDARY)
  private Object lowerBoundary;

  public static final String SERIALIZED_NAME_PARTICIPANTS_COUNT = "participantsCount";
  @SerializedName(SERIALIZED_NAME_PARTICIPANTS_COUNT)
  private String participantsCount;

  public static final String SERIALIZED_NAME_STD_DEV = "stdDev";
  @SerializedName(SERIALIZED_NAME_STD_DEV)
  private Object stdDev;

  public static final String SERIALIZED_NAME_SUB_PRICE_DIFF = "subPriceDiff";
  @SerializedName(SERIALIZED_NAME_SUB_PRICE_DIFF)
  private Object subPriceDiff;

  public static final String SERIALIZED_NAME_UPPER_BOUNDARY = "upperBoundary";
  @SerializedName(SERIALIZED_NAME_UPPER_BOUNDARY)
  private Object upperBoundary;

  public TitaniumAllParticipantExplorerTableColumn() { 
  }

  public TitaniumAllParticipantExplorerTableColumn absDiffFromConsensusPrice(Object absDiffFromConsensusPrice) {
    
    this.absDiffFromConsensusPrice = absDiffFromConsensusPrice;
    return this;
  }

   /**
   * Get absDiffFromConsensusPrice
   * @return absDiffFromConsensusPrice
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getAbsDiffFromConsensusPrice() {
    return absDiffFromConsensusPrice;
  }


  public void setAbsDiffFromConsensusPrice(Object absDiffFromConsensusPrice) {
    this.absDiffFromConsensusPrice = absDiffFromConsensusPrice;
  }


  public TitaniumAllParticipantExplorerTableColumn consensusPrice(Object consensusPrice) {
    
    this.consensusPrice = consensusPrice;
    return this;
  }

   /**
   * Get consensusPrice
   * @return consensusPrice
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getConsensusPrice() {
    return consensusPrice;
  }


  public void setConsensusPrice(Object consensusPrice) {
    this.consensusPrice = consensusPrice;
  }


  public TitaniumAllParticipantExplorerTableColumn lowerBoundary(Object lowerBoundary) {
    
    this.lowerBoundary = lowerBoundary;
    return this;
  }

   /**
   * Get lowerBoundary
   * @return lowerBoundary
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getLowerBoundary() {
    return lowerBoundary;
  }


  public void setLowerBoundary(Object lowerBoundary) {
    this.lowerBoundary = lowerBoundary;
  }


  public TitaniumAllParticipantExplorerTableColumn participantsCount(String participantsCount) {
    
    this.participantsCount = participantsCount;
    return this;
  }

   /**
   * Get participantsCount
   * @return participantsCount
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getParticipantsCount() {
    return participantsCount;
  }


  public void setParticipantsCount(String participantsCount) {
    this.participantsCount = participantsCount;
  }


  public TitaniumAllParticipantExplorerTableColumn stdDev(Object stdDev) {
    
    this.stdDev = stdDev;
    return this;
  }

   /**
   * Get stdDev
   * @return stdDev
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getStdDev() {
    return stdDev;
  }


  public void setStdDev(Object stdDev) {
    this.stdDev = stdDev;
  }


  public TitaniumAllParticipantExplorerTableColumn subPriceDiff(Object subPriceDiff) {
    
    this.subPriceDiff = subPriceDiff;
    return this;
  }

   /**
   * Get subPriceDiff
   * @return subPriceDiff
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getSubPriceDiff() {
    return subPriceDiff;
  }


  public void setSubPriceDiff(Object subPriceDiff) {
    this.subPriceDiff = subPriceDiff;
  }


  public TitaniumAllParticipantExplorerTableColumn upperBoundary(Object upperBoundary) {
    
    this.upperBoundary = upperBoundary;
    return this;
  }

   /**
   * Get upperBoundary
   * @return upperBoundary
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getUpperBoundary() {
    return upperBoundary;
  }


  public void setUpperBoundary(Object upperBoundary) {
    this.upperBoundary = upperBoundary;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumAllParticipantExplorerTableColumn titaniumAllParticipantExplorerTableColumn = (TitaniumAllParticipantExplorerTableColumn) o;
    return Objects.equals(this.absDiffFromConsensusPrice, titaniumAllParticipantExplorerTableColumn.absDiffFromConsensusPrice) &&
        Objects.equals(this.consensusPrice, titaniumAllParticipantExplorerTableColumn.consensusPrice) &&
        Objects.equals(this.lowerBoundary, titaniumAllParticipantExplorerTableColumn.lowerBoundary) &&
        Objects.equals(this.participantsCount, titaniumAllParticipantExplorerTableColumn.participantsCount) &&
        Objects.equals(this.stdDev, titaniumAllParticipantExplorerTableColumn.stdDev) &&
        Objects.equals(this.subPriceDiff, titaniumAllParticipantExplorerTableColumn.subPriceDiff) &&
        Objects.equals(this.upperBoundary, titaniumAllParticipantExplorerTableColumn.upperBoundary);
  }

  @Override
  public int hashCode() {
    return Objects.hash(absDiffFromConsensusPrice, consensusPrice, lowerBoundary, participantsCount, stdDev, subPriceDiff, upperBoundary);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumAllParticipantExplorerTableColumn {\n");
    sb.append("    absDiffFromConsensusPrice: ").append(toIndentedString(absDiffFromConsensusPrice)).append("\n");
    sb.append("    consensusPrice: ").append(toIndentedString(consensusPrice)).append("\n");
    sb.append("    lowerBoundary: ").append(toIndentedString(lowerBoundary)).append("\n");
    sb.append("    participantsCount: ").append(toIndentedString(participantsCount)).append("\n");
    sb.append("    stdDev: ").append(toIndentedString(stdDev)).append("\n");
    sb.append("    subPriceDiff: ").append(toIndentedString(subPriceDiff)).append("\n");
    sb.append("    upperBoundary: ").append(toIndentedString(upperBoundary)).append("\n");
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
    openapiFields.add("absDiffFromConsensusPrice");
    openapiFields.add("consensusPrice");
    openapiFields.add("lowerBoundary");
    openapiFields.add("participantsCount");
    openapiFields.add("stdDev");
    openapiFields.add("subPriceDiff");
    openapiFields.add("upperBoundary");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumAllParticipantExplorerTableColumn
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumAllParticipantExplorerTableColumn.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumAllParticipantExplorerTableColumn is not found in the empty JSON string", TitaniumAllParticipantExplorerTableColumn.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumAllParticipantExplorerTableColumn.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumAllParticipantExplorerTableColumn` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      if (jsonObj.get("participantsCount") != null && !jsonObj.get("participantsCount").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `participantsCount` to be a primitive type in the JSON string but got `%s`", jsonObj.get("participantsCount").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumAllParticipantExplorerTableColumn.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumAllParticipantExplorerTableColumn' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumAllParticipantExplorerTableColumn> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumAllParticipantExplorerTableColumn.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumAllParticipantExplorerTableColumn>() {
           @Override
           public void write(JsonWriter out, TitaniumAllParticipantExplorerTableColumn value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumAllParticipantExplorerTableColumn read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumAllParticipantExplorerTableColumn given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumAllParticipantExplorerTableColumn
  * @throws IOException if the JSON string is invalid with respect to TitaniumAllParticipantExplorerTableColumn
  */
  public static TitaniumAllParticipantExplorerTableColumn fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumAllParticipantExplorerTableColumn.class);
  }

 /**
  * Convert an instance of TitaniumAllParticipantExplorerTableColumn to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

