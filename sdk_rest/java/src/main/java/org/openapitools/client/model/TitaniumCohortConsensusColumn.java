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
 * TitaniumCohortConsensusColumn
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-08-24T16:35:00.030839Z[UTC]")
public class TitaniumCohortConsensusColumn {
  public static final String SERIALIZED_NAME_ABS_DIFF_FROM_CONSENSUS = "absDiffFromConsensus";
  @SerializedName(SERIALIZED_NAME_ABS_DIFF_FROM_CONSENSUS)
  private Object absDiffFromConsensus;

  public static final String SERIALIZED_NAME_ACCEPTED_MAX = "acceptedMax";
  @SerializedName(SERIALIZED_NAME_ACCEPTED_MAX)
  private Object acceptedMax;

  public static final String SERIALIZED_NAME_ACCEPTED_MIN = "acceptedMin";
  @SerializedName(SERIALIZED_NAME_ACCEPTED_MIN)
  private Object acceptedMin;

  public static final String SERIALIZED_NAME_COHORT_CONSENSUS_PRICE = "cohortConsensusPrice";
  @SerializedName(SERIALIZED_NAME_COHORT_CONSENSUS_PRICE)
  private Object cohortConsensusPrice;

  public static final String SERIALIZED_NAME_CONS_ABS_DIFF_FROM_ANCHOR_EVP_MID = "consAbsDiffFromAnchorEvpMid";
  @SerializedName(SERIALIZED_NAME_CONS_ABS_DIFF_FROM_ANCHOR_EVP_MID)
  private Object consAbsDiffFromAnchorEvpMid;

  public static final String SERIALIZED_NAME_CONS_ABS_DIFF_FROM_ANCHOR_EVP_MID_CALC = "consAbsDiffFromAnchorEvpMidCalc";
  @SerializedName(SERIALIZED_NAME_CONS_ABS_DIFF_FROM_ANCHOR_EVP_MID_CALC)
  private Object consAbsDiffFromAnchorEvpMidCalc;

  public static final String SERIALIZED_NAME_CONS_ABS_DIFF_FROM_ANCHOR_SUB = "consAbsDiffFromAnchorSub";
  @SerializedName(SERIALIZED_NAME_CONS_ABS_DIFF_FROM_ANCHOR_SUB)
  private Object consAbsDiffFromAnchorSub;

  public static final String SERIALIZED_NAME_CONS_ABS_DIFF_FROM_ANCHOR_TRADE = "consAbsDiffFromAnchorTrade";
  @SerializedName(SERIALIZED_NAME_CONS_ABS_DIFF_FROM_ANCHOR_TRADE)
  private Object consAbsDiffFromAnchorTrade;

  public static final String SERIALIZED_NAME_NUMBER_OF_INSTRUMENTS = "numberOfInstruments";
  @SerializedName(SERIALIZED_NAME_NUMBER_OF_INSTRUMENTS)
  private Object numberOfInstruments;

  public static final String SERIALIZED_NAME_STD_DEV = "stdDev";
  @SerializedName(SERIALIZED_NAME_STD_DEV)
  private Object stdDev;

  public static final String SERIALIZED_NAME_SUB_PRICE_DIFF = "subPriceDiff";
  @SerializedName(SERIALIZED_NAME_SUB_PRICE_DIFF)
  private Object subPriceDiff;

  public TitaniumCohortConsensusColumn() { 
  }

  public TitaniumCohortConsensusColumn absDiffFromConsensus(Object absDiffFromConsensus) {
    
    this.absDiffFromConsensus = absDiffFromConsensus;
    return this;
  }

   /**
   * Get absDiffFromConsensus
   * @return absDiffFromConsensus
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getAbsDiffFromConsensus() {
    return absDiffFromConsensus;
  }


  public void setAbsDiffFromConsensus(Object absDiffFromConsensus) {
    this.absDiffFromConsensus = absDiffFromConsensus;
  }


  public TitaniumCohortConsensusColumn acceptedMax(Object acceptedMax) {
    
    this.acceptedMax = acceptedMax;
    return this;
  }

   /**
   * Get acceptedMax
   * @return acceptedMax
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getAcceptedMax() {
    return acceptedMax;
  }


  public void setAcceptedMax(Object acceptedMax) {
    this.acceptedMax = acceptedMax;
  }


  public TitaniumCohortConsensusColumn acceptedMin(Object acceptedMin) {
    
    this.acceptedMin = acceptedMin;
    return this;
  }

   /**
   * Get acceptedMin
   * @return acceptedMin
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getAcceptedMin() {
    return acceptedMin;
  }


  public void setAcceptedMin(Object acceptedMin) {
    this.acceptedMin = acceptedMin;
  }


  public TitaniumCohortConsensusColumn cohortConsensusPrice(Object cohortConsensusPrice) {
    
    this.cohortConsensusPrice = cohortConsensusPrice;
    return this;
  }

   /**
   * Get cohortConsensusPrice
   * @return cohortConsensusPrice
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getCohortConsensusPrice() {
    return cohortConsensusPrice;
  }


  public void setCohortConsensusPrice(Object cohortConsensusPrice) {
    this.cohortConsensusPrice = cohortConsensusPrice;
  }


  public TitaniumCohortConsensusColumn consAbsDiffFromAnchorEvpMid(Object consAbsDiffFromAnchorEvpMid) {
    
    this.consAbsDiffFromAnchorEvpMid = consAbsDiffFromAnchorEvpMid;
    return this;
  }

   /**
   * Get consAbsDiffFromAnchorEvpMid
   * @return consAbsDiffFromAnchorEvpMid
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getConsAbsDiffFromAnchorEvpMid() {
    return consAbsDiffFromAnchorEvpMid;
  }


  public void setConsAbsDiffFromAnchorEvpMid(Object consAbsDiffFromAnchorEvpMid) {
    this.consAbsDiffFromAnchorEvpMid = consAbsDiffFromAnchorEvpMid;
  }


  public TitaniumCohortConsensusColumn consAbsDiffFromAnchorEvpMidCalc(Object consAbsDiffFromAnchorEvpMidCalc) {
    
    this.consAbsDiffFromAnchorEvpMidCalc = consAbsDiffFromAnchorEvpMidCalc;
    return this;
  }

   /**
   * Get consAbsDiffFromAnchorEvpMidCalc
   * @return consAbsDiffFromAnchorEvpMidCalc
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getConsAbsDiffFromAnchorEvpMidCalc() {
    return consAbsDiffFromAnchorEvpMidCalc;
  }


  public void setConsAbsDiffFromAnchorEvpMidCalc(Object consAbsDiffFromAnchorEvpMidCalc) {
    this.consAbsDiffFromAnchorEvpMidCalc = consAbsDiffFromAnchorEvpMidCalc;
  }


  public TitaniumCohortConsensusColumn consAbsDiffFromAnchorSub(Object consAbsDiffFromAnchorSub) {
    
    this.consAbsDiffFromAnchorSub = consAbsDiffFromAnchorSub;
    return this;
  }

   /**
   * Get consAbsDiffFromAnchorSub
   * @return consAbsDiffFromAnchorSub
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getConsAbsDiffFromAnchorSub() {
    return consAbsDiffFromAnchorSub;
  }


  public void setConsAbsDiffFromAnchorSub(Object consAbsDiffFromAnchorSub) {
    this.consAbsDiffFromAnchorSub = consAbsDiffFromAnchorSub;
  }


  public TitaniumCohortConsensusColumn consAbsDiffFromAnchorTrade(Object consAbsDiffFromAnchorTrade) {
    
    this.consAbsDiffFromAnchorTrade = consAbsDiffFromAnchorTrade;
    return this;
  }

   /**
   * Get consAbsDiffFromAnchorTrade
   * @return consAbsDiffFromAnchorTrade
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getConsAbsDiffFromAnchorTrade() {
    return consAbsDiffFromAnchorTrade;
  }


  public void setConsAbsDiffFromAnchorTrade(Object consAbsDiffFromAnchorTrade) {
    this.consAbsDiffFromAnchorTrade = consAbsDiffFromAnchorTrade;
  }


  public TitaniumCohortConsensusColumn numberOfInstruments(Object numberOfInstruments) {
    
    this.numberOfInstruments = numberOfInstruments;
    return this;
  }

   /**
   * Get numberOfInstruments
   * @return numberOfInstruments
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getNumberOfInstruments() {
    return numberOfInstruments;
  }


  public void setNumberOfInstruments(Object numberOfInstruments) {
    this.numberOfInstruments = numberOfInstruments;
  }


  public TitaniumCohortConsensusColumn stdDev(Object stdDev) {
    
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


  public TitaniumCohortConsensusColumn subPriceDiff(Object subPriceDiff) {
    
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



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumCohortConsensusColumn titaniumCohortConsensusColumn = (TitaniumCohortConsensusColumn) o;
    return Objects.equals(this.absDiffFromConsensus, titaniumCohortConsensusColumn.absDiffFromConsensus) &&
        Objects.equals(this.acceptedMax, titaniumCohortConsensusColumn.acceptedMax) &&
        Objects.equals(this.acceptedMin, titaniumCohortConsensusColumn.acceptedMin) &&
        Objects.equals(this.cohortConsensusPrice, titaniumCohortConsensusColumn.cohortConsensusPrice) &&
        Objects.equals(this.consAbsDiffFromAnchorEvpMid, titaniumCohortConsensusColumn.consAbsDiffFromAnchorEvpMid) &&
        Objects.equals(this.consAbsDiffFromAnchorEvpMidCalc, titaniumCohortConsensusColumn.consAbsDiffFromAnchorEvpMidCalc) &&
        Objects.equals(this.consAbsDiffFromAnchorSub, titaniumCohortConsensusColumn.consAbsDiffFromAnchorSub) &&
        Objects.equals(this.consAbsDiffFromAnchorTrade, titaniumCohortConsensusColumn.consAbsDiffFromAnchorTrade) &&
        Objects.equals(this.numberOfInstruments, titaniumCohortConsensusColumn.numberOfInstruments) &&
        Objects.equals(this.stdDev, titaniumCohortConsensusColumn.stdDev) &&
        Objects.equals(this.subPriceDiff, titaniumCohortConsensusColumn.subPriceDiff);
  }

  @Override
  public int hashCode() {
    return Objects.hash(absDiffFromConsensus, acceptedMax, acceptedMin, cohortConsensusPrice, consAbsDiffFromAnchorEvpMid, consAbsDiffFromAnchorEvpMidCalc, consAbsDiffFromAnchorSub, consAbsDiffFromAnchorTrade, numberOfInstruments, stdDev, subPriceDiff);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumCohortConsensusColumn {\n");
    sb.append("    absDiffFromConsensus: ").append(toIndentedString(absDiffFromConsensus)).append("\n");
    sb.append("    acceptedMax: ").append(toIndentedString(acceptedMax)).append("\n");
    sb.append("    acceptedMin: ").append(toIndentedString(acceptedMin)).append("\n");
    sb.append("    cohortConsensusPrice: ").append(toIndentedString(cohortConsensusPrice)).append("\n");
    sb.append("    consAbsDiffFromAnchorEvpMid: ").append(toIndentedString(consAbsDiffFromAnchorEvpMid)).append("\n");
    sb.append("    consAbsDiffFromAnchorEvpMidCalc: ").append(toIndentedString(consAbsDiffFromAnchorEvpMidCalc)).append("\n");
    sb.append("    consAbsDiffFromAnchorSub: ").append(toIndentedString(consAbsDiffFromAnchorSub)).append("\n");
    sb.append("    consAbsDiffFromAnchorTrade: ").append(toIndentedString(consAbsDiffFromAnchorTrade)).append("\n");
    sb.append("    numberOfInstruments: ").append(toIndentedString(numberOfInstruments)).append("\n");
    sb.append("    stdDev: ").append(toIndentedString(stdDev)).append("\n");
    sb.append("    subPriceDiff: ").append(toIndentedString(subPriceDiff)).append("\n");
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
    openapiFields.add("absDiffFromConsensus");
    openapiFields.add("acceptedMax");
    openapiFields.add("acceptedMin");
    openapiFields.add("cohortConsensusPrice");
    openapiFields.add("consAbsDiffFromAnchorEvpMid");
    openapiFields.add("consAbsDiffFromAnchorEvpMidCalc");
    openapiFields.add("consAbsDiffFromAnchorSub");
    openapiFields.add("consAbsDiffFromAnchorTrade");
    openapiFields.add("numberOfInstruments");
    openapiFields.add("stdDev");
    openapiFields.add("subPriceDiff");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumCohortConsensusColumn
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumCohortConsensusColumn.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumCohortConsensusColumn is not found in the empty JSON string", TitaniumCohortConsensusColumn.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumCohortConsensusColumn.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumCohortConsensusColumn` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumCohortConsensusColumn.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumCohortConsensusColumn' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumCohortConsensusColumn> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumCohortConsensusColumn.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumCohortConsensusColumn>() {
           @Override
           public void write(JsonWriter out, TitaniumCohortConsensusColumn value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumCohortConsensusColumn read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumCohortConsensusColumn given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumCohortConsensusColumn
  * @throws IOException if the JSON string is invalid with respect to TitaniumCohortConsensusColumn
  */
  public static TitaniumCohortConsensusColumn fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumCohortConsensusColumn.class);
  }

 /**
  * Convert an instance of TitaniumCohortConsensusColumn to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

